from collections import defaultdict

from flask import jsonify, request
from index import app, db
from models import PostalCode
from serializers import PostalCodeSchema


@app.route('/paystats', methods=['GET'])
def paystats():
    """
    Returns a payload with postal codes with paystats data by postal code.
    """
    code = request.args.get('code')
    if code:
        pcode = PostalCode.query.filter_by(code=code).first()
        result = PostalCodeSchema().dump(pcode)
    else:
        pcodes = PostalCode.query.all()[:10]
        result = PostalCodeSchema(many=True).dump(pcodes)

    return jsonify(result.data)


@app.route('/total', methods=['GET'])
def total():
    """
    Returns a payload with total amount.
    """
    code = request.args.get('code')

    sql_body = """
        SELECT SUM(PS.amount)
        FROM postal_codes PC LEFT JOIN paystats PS
        ON PC.id = PS.postal_code_id
    """
    where = " WHERE PC.code = '{}'".format(code) if code else ''

    sql = sql_body + where

    result = db.engine.execute(sql).fetchone()[0]
    return jsonify(dict(total=int(result)))


@app.route('/test', methods=['GET'])
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

    # pcodes = PostalCode.query.all()[:10]
    # postal_codes = PostalCodeSchema(many=True).dump(pcodes)

    # for item in postal_codes.data:
    #     item.update(dict(paystats=out[item['code']]))
    return jsonify(out)


if __name__ == '__main__':
    app.run()
