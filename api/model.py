from api import db


class Agency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40))
    domain = db.Column(db.String(50))
    address = db.Column(db.String(80))

    def __init__(self, agency_id, title, domain, address):
        self.id = agency_id
        self.title = title
        self.domain = domain
        self.address = address


class Broker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    agency_id = db.Column(db.Integer, db.ForeignKey("agency.id"))
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(40))
    email = db.Column(db.String(50), unique=True)
    address = db.Column(db.String(80))

    def __init__(self, first_name, last_name, email, address):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address


class AgencyDomainWhiteList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String(50))

    def __init__(self, domain_id, domain):
        self.id = domain_id
        self.domain = domain


class BrokerWithAgency:
    def __init__(self, title, domain, first_name, last_name, email, address):
        self.title = title
        self.domain = domain
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
