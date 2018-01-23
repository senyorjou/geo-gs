from index import db


class Paystats(db.Model):
    __tablename__ = 'paystats'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Numeric(20, 10))
    p_month = db.Column(db.Date)
    p_age = db.Column(db.String)
    p_gender = db.Column(db.String)
    postal_code_id = db.Column(db.Integer, db.ForeignKey('postal_codes.id'))


class PostalCode(db.Model):
    __tablename__ = 'postal_codes'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String)
    the_geom = db.Column(db.Text)
