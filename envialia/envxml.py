#This file is part of envialia. The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.

from datetime import date


class ENVXML(object):
    """
    Generic XML data Envialia API
    """
    __slots__ = ()

    def envialia_xml_login(self, agency, customer, password):
        """
        Envialia XML Login
        """
        xml = '<?xml version="1.0" encoding="utf-8"?>' \
        '<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">' \
        '<soap:Body>' \
        '<LoginWSService___LoginCli>' \
        '<strCodAge>%(agency)s</strCodAge>' \
        '<strCod>%(customer)s</strCod>' \
        '<strPass>%(password)s</strPass>' \
        '</LoginWSService___LoginCli>' \
        '</soap:Body>' \
        '</soap:Envelope>' % {
            'agency': agency,
            'customer': customer,
            'password': password,
        }
        return xml

    def envialia_xml_picking_list(self, session, date):
        """
        Envialia XML Picking List (InfEnvios)
        """
        xml = '<?xml version="1.0" encoding="utf-8"?>' \
        '<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">' \
        '<soap:Header>' \
        '<ROClientIDHeader xmlns="http://tempuri.org/">' \
        '<ID>%(session)s</ID>' \
        '</ROClientIDHeader>' \
        '</soap:Header>' \
        '<soap:Body>' \
        '<WebServService___InfEnvios>' \
        '<dtFecha>%(date)s</dtFecha>' \
        '</WebServService___InfEnvios>' \
        '</soap:Body>' \
        '</soap:Envelope>' % {
            'session': session,
            'date': date,
        }
        return xml

    def envialia_xml_picking_info(self, session, reference, data):
        """
        Envialia XML Picking Info (ConsEnvio)
        """

        xml = '<?xml version="1.0" encoding="utf-8"?>' \
        '<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">' \
        '<soap:Header>' \
        '<ROClientIDHeader xmlns="http://tempuri.org/">' \
        '<ID>%(session)s</ID>' \
        '</ROClientIDHeader>' \
        '</soap:Header>' \
        '<soap:Body>' \
        '<WebServService___ConsEnvio>' \
        '<strCodAgeCargo>%(agency_cargo)s</strCodAgeCargo>' \
        '<strCodAgeOri>%(agency_origin)s</strCodAgeOri>' \
        '<strAlbaran>%(reference)s</strAlbaran>' \
        '</WebServService___ConsEnvio>' \
        '</soap:Body>' \
        '</soap:Envelope>' % {
            'session': session,
            'agency_cargo': data.get('agency_cargo', ''),
            'agency_origin': data.get('agency_origin', ''),
            'reference': reference,
        }
        return xml

    def envialia_xml_picking_state(self, session, reference, data):
        """
        Envialia XML Picking State (ConsEnvEstados)
        """
        xml = '<?xml version="1.0" encoding="utf-8"?>' \
        '<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">' \
        '<soap:Header>' \
        '<ROClientIDHeader xmlns="http://tempuri.org/">' \
        '<ID>%(session)s</ID>' \
        '</ROClientIDHeader>' \
        '</soap:Header>' \
        '<soap:Body>' \
        '<WebServService___ConsEnvEstados>' \
        '<strCodAgeCargo>%(agency_cargo)s</strCodAgeCargo>' \
        '<strCodAgeOri>%(agency_origin)s</strCodAgeOri>' \
        '<strAlbaran>%(reference)s</strAlbaran>' \
        '</WebServService___ConsEnvEstados>' \
        '</soap:Body>' \
        '</soap:Envelope>' % {
            'session': session,
            'agency_cargo': data.get('agency_cargo', ''),
            'agency_origin': data.get('agency_origin', ''),
            'reference': reference,
        }
        return xml

    def envialia_xml_picking_create(self, session, data):
        """
        Envialia XML Picking Create (GrabaEnvio5)
        """
        xml = '<?xml version="1.0" encoding="utf-8"?>' \
        '<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">' \
        '<soap:Header>' \
        '<ROClientIDHeader xmlns="http://tempuri.org/">' \
        '<ID>%(session)s</ID>' \
        '</ROClientIDHeader>' \
        '</soap:Header>' \
        '<soap:Body>' \
        '<WebServService___GrabaEnvio7 xmlns="http://tempuri.org/">' \
        '<strCodAgeCargo>%(agency_cargo)s</strCodAgeCargo>' \
        '<strCodAgeOri>%(agency_origin)s</strCodAgeOri>' \
        '<strAlbaran>%(reference)s</strAlbaran>' \
        '<dtFecha>%(picking_date)s</dtFecha>' \
        '<strCodAgeDes>%(agency_dest)s</strCodAgeDes>' \
        '<strCodTipoServ>%(service_code)s</strCodTipoServ>' \
        '<strCodCli>%(company_code)s</strCodCli>' \
        '<strCodCliDep>%(department_code)s</strCodCliDep>' \
        '<strNomOri>%(company_name)s</strNomOri>' \
        '<strTipoViaOri>%(company_street_type)s</strTipoViaOri>' \
        '<strDirOri>%(company_street)s</strDirOri>' \
        '<strNumOri>%(company_street_number)s</strNumOri>' \
        '<strPisoOri>%(company_street_floor)s</strPisoOri>' \
        '<strPobOri>%(company_city)s</strPobOri>' \
        '<strCPOri>%(company_zip)s</strCPOri>' \
        '<strCodProOri>%(company_subdivision_code)s</strCodProOri>' \
        '<strTlfOri>%(company_phone)s</strTlfOri>' \
        '<strNomDes>%(customer_name)s</strNomDes>' \
        '<strTipoViaDes>%(customer_street_type)s</strTipoViaDes>' \
        '<strDirDes>%(customer_street)s</strDirDes>' \
        '<strNumDes>%(customer_street_number)s</strNumDes>' \
        '<strPisoDes>%(customer_street_floor)s</strPisoDes>' \
        '<strPobDes>%(customer_city)s</strPobDes>' \
        '<strCPDes>%(customer_zip)s</strCPDes>' \
        '<strTlfDes>%(customer_phone)s</strTlfDes>' \
        '<intDoc>%(document)s</intDoc>' \
        '<intPaq>%(packages)s</intPaq>' \
        '<dPesoOri>%(weight)s</dPesoOri>' \
        '<dAltoOri>%(height)s</dAltoOri>' \
        '<dAnchoOri>%(width)s</dAnchoOri>' \
        '<dLargoOri>%(large)s</dLargoOri>' \
        '<dReembolso>%(cash_ondelivery)s</dReembolso>' \
        '<dValor>%(total)s</dValor>' \
        '<dAnticipo>%(advance)s</dAnticipo>' \
        '<dCobCli>%(customer_total)s</dCobCli>' \
        '<strObs>%(notes)s</strObs>' \
        '<boSabado>%(saturday)s</boSabado>' \
        '<boRetorno>%(return)s</boRetorno>' \
        '<boGestOri>%(to)s</boGestOri>' \
        '<boGestDes>%(from)s</boGestDes>' \
        '<boAnulado>%(canceled)s</boAnulado>' \
        '<boAcuse>%(receipt)s</boAcuse>' \
        '<strCodRep>%(delivery_code)s</strCodRep>' \
        '<strRef>%(ref)s</strRef>' \
        '<strCodSalRuta>%(way_code)s</strCodSalRuta>' \
        '<dBaseImp>%(amount_total)s</dBaseImp>' \
        '<dImpuesto>%(amount_tax)s</dImpuesto>' \
        '<boPorteDebCli>%(customer_total)s</boPorteDebCli>' \
        '<strPersContacto>%(customer_contact_name)s</strPersContacto>' \
        '<strCodPais>%(customer_state)s</strCodPais>' \
        '<strDesMoviles>%(customer_mobile)s</strDesMoviles>' \
        '<strDesDirEmails>%(customer_email)s</strDesDirEmails>' \
        '<boInsert>%(insert)s</boInsert>' \
        '<strFranjaHoraria>%(gtm)s</strFranjaHoraria>' \
        '<dtHoraEnvIni>%(delivery_start)s</dtHoraEnvIni>' \
        '<dtHoraEnvFin>%(delivery_finish)s</dtHoraEnvFin>' \
        '</WebServService___GrabaEnvio7>' \
        '</soap:Body>' \
        '</soap:Envelope>' % {
            'session': session,
            'agency_cargo': data.get('agency_cargo', ''),
            'agency_origin': data.get('agency_origin', ''),
            'reference': data.get('reference', ''),
            'picking_date': data.get('picking_date', date.today()),
            'agency_dest': data.get('agency_dest', ''),
            'service_code': data.get('service_code', ''),
            'company_code': data.get('company_code', ''),
            'department_code': data.get('department_code', ''),
            'company_name': data.get('company_name', ''),
            'company_street_type': data.get('company_street_type', ''),
            'company_street': data.get('company_street', ''),
            'company_street_number': data.get('company_street_number', ''),
            'company_street_floor': data.get('company_street_floor', ''),
            'company_city': data.get('company_city', ''),
            'company_zip': data.get('companyr_zip', ''),
            'company_subdivision_code': data.get('company_subdivision_code', ''),
            'company_phone': data.get('company_phone', ''),
            'customer_name': data.get('customer_name', ''),
            'customer_street_type': data.get('customer_street_type', ''),
            'customer_street': data.get('customer_street', ''),
            'customer_street_number': data.get('customer_street_number', ''),
            'customer_street_floor': data.get('customer_street_floor', ''),
            'customer_city': data.get('customer_city', ''),
            'customer_zip': data.get('customer_zip', ''),
            'customer_phone': data.get('customer_phone', ''),
            'document': data.get('document', 1),
            'packages': data.get('packages', 0),
            'weight': data.get('weight', 0),
            'height': data.get('height', 0),
            'width': data.get('width', 0),
            'large': data.get('large', 0),
            'cash_ondelivery': data.get('cash_ondelivery', 0),
            'total': data.get('total', 0),
            'advance': data.get('advance', 0),
            'customer_total': data.get('customer_total', 0),
            'notes': data.get('notes', ''),
            'saturday': data.get('saturday', False),
            'return': data.get('return', False),
            'to': data.get('to', False),
            'from': data.get('from', False),
            'canceled': data.get('canceled', False),
            'receipt': data.get('receipt', False),
            'delivery_code': data.get('delivery_code', ''),
            'ref': data.get('ref', ''),
            'way_code': data.get('way_code', ''),
            'amount_total': data.get('amount_total', 0),
            'amount_tax': data.get('amount_tax', 0),
            'customer_total': data.get('customer_total', 0),
            'customer_contact_name': data.get('customer_contact_name', ''),
            'customer_state': data.get('customer_state', ''),
            'customer_mobile': data.get('customer_mobile', ''),
            'customer_email': data.get('customer_email', ''),
            'insert': data.get('insert', True),
            'gtm': data.get('gtm', ''),
            'delivery_start': data.get('delivery_start', ''),
            'delivery_finish': data.get('delivery_finish', ''),
        }
        return xml

    def envialia_xml_picking_delete(self, session, reference, data):
        """
        Envialia XML Picking Delete (BorraEnvio)
        """
        xml = '<?xml version="1.0" encoding="utf-8"?>' \
        '<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchemainstance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">' \
        '<soap:Header>' \
        '<ROClientIDHeader xmlns="http://tempuri.org/">' \
        '<ID>%(session)s</ID>' \
        '</ROClientIDHeader>' \
        '</soap:Header>' \
        '<soap:Body>' \
        '<WebServService___BorraEnvio xmlns="http://tempuri.org/">' \
        '<strCodAgeCargo>%(agency_cargo)s</strCodAgeCargo>' \
        '<strCodAgeOri>%(agency_origin)s</strCodAgeOri>' \
        '<strAlbaran>%(reference)s</strAlbaran>' \
        '</WebServService___BorraEnvio>' \
        '</soap:Body>' \
        '</soap:Envelope>' % {
            'session': session,
            'agency_cargo': data.get('agency_cargo', ''),
            'agency_origin': data.get('agency_origin', ''),
            'reference': reference,
        }
        return xml

    def envialia_xml_picking_label(self, session, reference, data):
        """
        Envialia XML Picking Label (ConsEtiquetaEnvio)
        """
        xml = '<?xml version="1.0" encoding="utf-8"?>' \
        '<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">' \
        '<soap:Header>' \
        '<ROClientIDHeader xmlns="http://tempuri.org/">' \
        '<ID>%(session)s</ID>' \
        '</ROClientIDHeader>' \
        '</soap:Header>' \
        '<soap:Body>' \
        '<WebServService___ConsEtiquetaEnvio4>' \
        '<strCodAgeOri>%(agency_cargo)s</strCodAgeOri>' \
        '<strAlbaran>%(reference)s</strAlbaran>' \
        '</WebServService___ConsEtiquetaEnvio4>' \
        '</soap:Body>' \
        '</soap:Envelope>' % {
            'session': session,
            'agency_cargo': data.get('agency_cargo', ''),
            'reference': reference,
        }
        return xml
