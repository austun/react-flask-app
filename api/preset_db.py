from api import db
from model import AgencyDomainWhiteList, Agency


def main():
    db.drop_all()
    db.create_all()

    agency_domain_whitelist = [
        {'id': 1, 'domain': 'cyberrisksolved.com'},
        {'id': 2, 'domain': 'cyberinsurance.com'},
        {'id': 3, 'domain': 'cyberworld.com'},
        {'id': 4, 'domain': 'savefromcyber.com'},
        {'id': 5, 'domain': 'cyberunderwriting.com'}
    ]

    for agency_domain in agency_domain_whitelist:
        agency_domain_entity = AgencyDomainWhiteList(agency_domain.get('id'), agency_domain.get('domain'))

        db.session.add(agency_domain_entity)
        db.session.commit()

    agencies = [
        {'id': 1, 'title': 'Cyber Risk Solved Inc', 'domain': 'cyberrisksolved.com',
         'address': '4418 N Rancho Dr, Las Vegas, NV 89130'},
        {'id': 2, 'title': 'Cyber Insurance LLC', 'domain': 'cyberinsurance.com',
         'address': '2025 E Florence Ave, Los Angeles, CA 90001'},
        {'id': 3, 'title': 'Cyber World Inc, San Francisco', 'domain': 'cyberworld.com',
         'address': '876 Geary St, San Francisco, CA 94109'},
        {'id': 4, 'title': 'Cyber World Inc, New York', 'domain': 'cyberworld.com',
         'address': '148 W 72nd St, New York, NY 10023'},
        {'id': 5, 'title': 'Cyber World Inc, Miami', 'domain': 'cyberworld.com',
         'address': '1575 SW 8th St, Miami, FL 33135'}
    ]

    for agency in agencies:
        agency_entity = Agency(agency.get('id'), agency.get('title'), agency.get('domain'), agency.get('address'))

        db.session.add(agency_entity)
        db.session.commit()


if __name__ == '__main__':
    main()
