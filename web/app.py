from collections import defaultdict

from flask import jsonify, request

from index import app, auth, db, tokens
from models import PostalCode
from serializers import PostalCodeSchema


def auth_error_override():
    """
    Returns a custom error for unauthorized accesses.
    """
    response = jsonify({'genericErrors': ['Unauthorized access']})
    response.status_code = 401
    return response


# Override the authentication error response
auth.error_handler(auth_error_override)


@auth.verify_token
def verify_token(token):
    """
    Simple dead auth. Check `tokens` in index.py
    """
    if token in tokens:
        return True
    return False


@app.route('/paystats', methods=['GET'])
@auth.login_required
def paystats():
    """
    Returns a payload with postal codes with paystats data by postal code.
    """
    code = request.args.get('code')
    if code:
        pcode = PostalCode.query.filter_by(code=code).first()
        result = PostalCodeSchema().dump(pcode)
    else:
        pcodes = PostalCode.query.all()
        result = PostalCodeSchema(many=True).dump(pcodes)

    return jsonify(result.data)


@app.route('/total', methods=['GET'])
@auth.login_required
def total():
    """
    Returns a payload with total amount.
    """
    code = request.args.get('code')

    sql_where = " WHERE PC.code = '{}'".format(code) if code else ''
    sql = """
        SELECT SUM(PS.amount)
        FROM postal_codes PC LEFT JOIN paystats PS
        ON PC.id = PS.postal_code_id
        {sql_where}
    """.format(sql_where=sql_where)

    result = db.engine.execute(sql).fetchone()[0]
    return jsonify(dict(total=int(result)))


@app.route('/age_gender', methods=['GET'])
@auth.login_required
def age_gender():
    """
    Returns a payload with age & gender data.
    """
    code = request.args.get('code')

    sql_where = " WHERE PC.code = '{}'".format(code) if code else ''
    sql = """
        SELECT p_age, p_gender, sum(amount)
        {sql_where}
        FROM paystats PS LEFT JOIN postal_codes PC on PS.postal_code_id = PC.id
        GROUP BY p_age, p_gender
    """.format(sql_where=sql_where)

    out = defaultdict(dict)
    for age, gender, amount in db.engine.execute(sql):
        out[age][gender] = float(amount)

    return jsonify(out)


@app.route('/test', methods=['GET'])
@auth.login_required
def test():
    """
    Returns a payload with aggregated data for paystats by postal code
    """
    sql = """
        SELECT PC.code, PS.amount, PS.p_age, PS.p_gender
        FROM (
            SELECT postal_code_id, sum(amount) as amount, p_age, p_gender
            FROM paystats
            GROUP BY postal_code_id, p_age, p_gender
        ) PS JOIN postal_codes PC ON PC.id = PS.postal_code_id
        ORDER BY PC.code, PS.p_age, PS.p_gender;
    """
    result = db.engine.execute(sql)

    out = defaultdict(dict)
    for pcode, value, age, gender in result:
        if age not in out[pcode]:
            out[pcode][age] = {gender: float(value)}
        else:
            out[pcode][age][gender] = float(value)

    return jsonify(out)


if __name__ == '__main__':
    app.run()
