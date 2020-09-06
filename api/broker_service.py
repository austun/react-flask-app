import re
import sys
from math import sin, cos, sqrt, atan2

import requests
from flask import jsonify
from sqlalchemy import exc

from api import db
from model import Broker, AgencyDomainWhiteList, Agency, BrokerWithAgency
from schema import broker_schema, brokers_with_agency_schema


def signup(data):
    is_invalid = validate_request(data)

    if is_invalid:
        return is_invalid

    broker = Broker(**data)
    domain = broker.email.split('@', 1)[1]

    try:
        query = db.session.query(AgencyDomainWhiteList).filter(AgencyDomainWhiteList.domain == domain)

        whitelist_domain = query.first()

        if whitelist_domain is None:
            return create_response(400, 'Broker domain does not exist in whitelist')

        query = db.session.query(Agency).filter(Agency.domain == domain)

        agencies = query.all()

        if agencies is None or len(agencies) == 0:
            return create_response(400, 'Broker domain does not match with any agency')

        number_of_agencies = len(agencies)

        if number_of_agencies > 1:
            broker_latitude, broker_longitude = get_coordinates_by_address(broker.address)
            min_distance = sys.maxsize

            for agency in agencies:
                agency_latitude, agency_longitude = get_coordinates_by_address(agency.address)

                distance = calculate_distance_by_coordinates(
                    broker_latitude,
                    broker_longitude,
                    agency_latitude,
                    agency_longitude
                )

                if distance < min_distance:
                    min_distance = distance
                    broker.agency_id = agency.id
        else:
            broker.agency_id = agencies[0].id

        db.session.add(broker)
        db.session.commit()

    except exc.SQLAlchemyError as exception:
        return create_response(400, exception.args[0])

    return broker_schema.jsonify(broker)


def get_brokers():
    try:
        query = db.session.query(Broker)

        brokers = query.all()

        broker_with_agencies = []

        for broker in brokers:
            query = db.session.query(Agency).filter(Agency.id == broker.agency_id)
            agency = query.first()

            if agency is None:
                return create_response(400, 'No agency found with given broker agency id')

            broker_with_agency = BrokerWithAgency(
                agency.title,
                agency.domain,
                broker.first_name,
                broker.last_name,
                broker.email,
                broker.address
            )

            broker_with_agencies.append(broker_with_agency)

    except exc.SQLAlchemyError as exception:
        return create_response(400, exception.args[0])

    return brokers_with_agency_schema.jsonify(broker_with_agencies)


def validate_request(data):
    for key in data.keys():
        is_valid = is_valid_text(data[key])

        if not is_valid:
            response_message = "%s should not be empty" % key
            return create_response(400, response_message)

    return is_valid_email(data['email'])


def is_valid_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if not re.search(regex, email):
        return create_response(400, 'Broker email address is not valid')


def is_valid_text(text):
    if text is None or text == "":
        return False

    return True


def get_coordinates_by_address(address):
    url = "https://geocode.search.hereapi.com/v1/geocode"
    api_key = 'AFhDmv9QFusjjdajF6daEcvgiCm2rGIjUFTDPG5xd-g'
    params = {'apikey': api_key, 'q': address}

    response = requests.get(url=url, params=params)
    data = response.json()

    latitude = data['items'][0]['position']['lat']
    longitude = data['items'][0]['position']['lng']

    return latitude, longitude


def calculate_distance_by_coordinates(lat1, lon1, lat2, lon2):
    r = 6373.0

    longitude_difference = lon2 - lon1
    latitude_difference = lat2 - lat1

    a = sin(latitude_difference / 2) ** 2 + cos(lat1) * cos(lat2) * sin(longitude_difference / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return r * c


def create_response(status_code, message):
    response = jsonify({
        'status': status_code,
        'message': message,
    })

    response.status_code = status_code

    return response
