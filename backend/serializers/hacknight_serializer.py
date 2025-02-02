from marshmallow import Schema, fields


class HacknightSchema(Schema):
    class Meta:
        fields = ('id', 'date', 'participants')
        dump_only = ('id',)

    participants = fields.Nested(
        'ParticipantSchema',
        exclude=('name', 'lastname', 'email', 'hacknights', 'phone'),
        many=True
    )
