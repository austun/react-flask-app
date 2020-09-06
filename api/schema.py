from api import ma


class BrokerSchema(ma.Schema):
    class Meta:
        fields = (
            'id',
            'agency_id',
            'first_name',
            'last_name',
            'email',
            'address'
        )


broker_schema = BrokerSchema()
brokers_schema = BrokerSchema(many=True)


class BrokerWithAgencySchema(ma.Schema):
    class Meta:
        fields = (
            'title',
            'domain',
            'first_name',
            'last_name',
            'email',
            'address'
        )


brokers_with_agency_schema = BrokerWithAgencySchema(many=True)
