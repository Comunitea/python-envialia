agency = ''
customer = ''
password = ''
debug = True

from envialia.picking import *

with API(agency, customer, password) as envialia_api:
    print "Test connection"
    print envialia_api.test_connection()

with Picking(agency, customer, password) as picking_api:
    date = '1899-12-01'
    print "Lista all pickings"
    print picking_api.list(date)

    reference = '12345'
    data = {}
    data['agency_origin'] = agency
    data['agency_cargo'] = agency
    print "Info Picking %s ----" % reference 
    print picking_api.info(reference, data)

    reference = '12345'
    data = {}
    data['agency_origin'] = agency
    data['agency_cargo'] = agency
    print "Info State %s ----" % reference 
    print picking_api.state(reference, data)

    print picking_api.delete(reference, data)
    print "Delete picking %s----" % reference
    # print picking_api.label(reference, data)

    data = {}
    data['agency_cargo'] = agency
    data['agency_origin'] = agency
    data['reference'] = '12345'
    # data['picking_date'] = '2012-11-05'
    data['agency_dest'] = agency
    data['service_code'] = 10
    data['customer_cp'] = '08720'

    data['company_code'] = 'Zikzakmedia'
    # data['department_code'] = ''
    data['customer_name'] = 'Raimon'
    # data['customer_street_type'] = ''
    data['customer_street'] = 'Dr. Fleming'
    data['customer_street_number'] = '28'
    data['customer_street_floor'] = '3,4'
    data['customer_city'] = 'Vilafranca'
    data['customer_zip'] = '08720'
    # data['customer_subdivision_code'] = ''
    data['company_phone'] = '938902108'
    data['customer_name'] = 'Raimon Esteve'
    data['customer_street_type'] = ''
    data['customer_street'] = 'Dr. Fleming'
    data['customer_street_number'] = '28'
    data['customer_street_floor'] = ''
    data['customer_city'] = 'Vilafranca'
    # data['customer_subdivision_code'] = ''
    data['customer_phone'] = '938902108'
    # data['document'] = 1
    # data['packages'] = 1
    # data['weight'] = 0
    # data['height'] = 0
    # data['width'] = 0
    # data['large'] = 0
    # data['refund'] = 0
    # data['total'] = 0
    # data['advance'] = 0
    # data['customer_total'] = 1.00
    # data['notes'] = ''
    # data['saturday'] = False
    # data['return'] = False
    # data['to'] = ''
    # data['from'] = ''
    # data['canceled'] = ''
    # data['receipt'] = ''
    # data['delivery_code'] = ''
    # data['way_code'] = ''
    # data['amount_total'] = ''
    # data['amount_tax'] = ''
    # data['customer_total'] = ''
    # data['customer_contact_name'] = ''
    # data['customer_state'] = ''
    # data['customer_mobile'] = ''
    # data['customer_email'] = ''
    # data['insert'] = ''
    # data['gtm'] = ''
    # data['delivery_start'] = ''
    # data['delivery_finish'] = ''
    print picking_api.create(data)


