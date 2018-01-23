from marshmallow import Schema, fields


class PostalCodeSchema(Schema):
    code = fields.String()
    the_geom = fields.String()


class PaystatsSchema(Schema):
    amount = fields.Decimal(places=2, as_string=True)
    p_month = fields.Date(required=True)
    p_age = fields.String()
    p_gender = fields.String()
    postal_code_id = fields.Integer(as_string=True)

    cocode = fields.Nested(PostalCodeSchema, required=True,
                           many=True, load_from='postal_code_id')
