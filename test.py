agency = ''
customer = ''
password = ''
debug = True

from envialia.picking import *
from envialia.utils import services

print "Envialia services"
services = services()
print services

with API(agency, customer, password, debug) as envialia_api:
    print "Test connection"
    print envialia_api.test_connection()

with Picking(agency, customer, password, debug) as picking_api:
    date = None  # date YYYY/MM/DD
    print "List all deliveries"
    print picking_api.list(date)

    data = {}
    data['agency_cargo'] = agency
    data['agency_origin'] = agency
    # data['reference'] = ''  # envialia use numbers in reference
    # data['picking_date'] = '2012/11/05' # not date, today
    # data['agency_dest'] = ''
    data['service_code'] = 10
    data['company_code'] = 'Zikzakmedia'
    data['customer_name'] = 'Raimon'
    data['customer_street'] = 'Dr. Fleming'
    data['customer_street_number'] = '28'
    data['customer_street_floor'] = 'Baixos'
    data['customer_city'] = 'Vilafranca del Penedes'
    data['customer_zip'] = '08720'
    data['company_phone'] = '938902108'
    picking_api.create(data)

    print "List all deliveries"
    date = None  # date YYYY/MM/DD
    deliveries = picking_api.list(date)

    data = {}
    data['agency_origin'] = agency
    data['agency_cargo'] = agency
    reference = deliveries[0]

    print "Delivery Info"
    print picking_api.info(reference, data)

    print "Delivery State"
    print picking_api.state(reference, data)

    print "Delivery delete"
    print picking_api.delete(reference, data)
