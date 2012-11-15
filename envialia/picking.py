#This file is part of envialia. The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.

from envialia.envxml import ENVXML
from envialia.api import API

from xml.dom.minidom import parseString
import re
import datetime

class Picking(API):
    """
    Picking API
    """
    __slots__ = ( )

    def list(self, date=None):
        """
        Retreive list of pickings a date (get all deliveries by date)

        :param date: String date YYYY/MM/DD

        :return: List delivery references
        """
        if not date:
            today = datetime.date.today()
            date = today.strftime('%Y/%m/%d')
        deliveries = []
        envxml = ENVXML()
        data = envxml.envialia_xml_picking_list(self.session, date)
        data = self.connect(data)
        dom = parseString(data)
        info = dom.getElementsByTagName('v1:strInfEnvios')
        if info[0].firstChild:
            info = info[0].firstChild.data
            info = re.sub('<CONSULTA><INF_ENVIOS ', '', info)
            info = re.sub('/></CONSULTA>', '', info)
            infos = info.split('" ')
            for inf in infos:
                i = inf.split('="')
                key = i[0]
                value = i[1]
                if key == 'V_ALBARAN':
                    deliveries.append(value)
        return deliveries

    def info(self, reference, data):
        """
        Retreive list of pickings a date

        :param date: String date YYYY-MM-DD

        :return: List of dictionaries of matching records
        """
        delivery = {}
        envxml = ENVXML()
        data = envxml.envialia_xml_picking_info(self.session, reference, data)
        data = self.connect(data)
        dom = parseString(data)
        info = dom.getElementsByTagName('v1:strEnvio')
        if info[0].firstChild:
            info = info[0].firstChild.data
            info = re.sub('<CONSULTA><ENVIOS ', '', info)
            info = re.sub('/></CONSULTA>', '', info)
            infos = info.split('" ')
            for inf in infos:
                i = inf.split("=")
                key = re.sub("'", '', i[0])
                value = i[1][1:]
                delivery[key] = value
        return delivery

    def create(self, data):
        """
        Create a picking using the given data

        :param data: Dictionary of values
        :return: Integer ID of new record
        """
        envxml = ENVXML()
        data = envxml.envialia_xml_picking_create(self.session, data)
        data = self.connect(data)
        return data

    def delete(self, reference, data):
        """
        Delete a picking using the reference

        :param reference: String Reference
        :param data: Dictionary of values
        :return: True/False
        """
        envxml = ENVXML()
        data = envxml.envialia_xml_picking_delete(self.session, reference, data)
        data = self.connect(data)
        dom = parseString(data)
        error = dom.getElementsByTagName('v1:intCodError')
        if error[0].firstChild:
            # return {'error':error[0].firstChild.data}
            return False
        return True

    def state(self, reference, data):
        """
        Get State picking using reference

        :param reference: String Reference
        :param data: Dictionary of values
        :return: String
        """
        envxml = ENVXML()
        data = envxml.envialia_xml_picking_state(self.session, reference, data)
        data = self.connect(data)
        dom = parseString(data)
        state = dom.getElementsByTagName('v1:strEnvEstados')
        if not state[0].firstChild:
            return None
        return state[0].firstChild.data

    def label(self, reference, data):
        """
        Get label picking using reference

        :param reference: String Reference
        :param data: Dictionary of values
        :return: String
        """
        envxml = ENVXML()
        data = envxml.envialia_xml_picking_label(self.session, reference, data)
        data = self.connect(data)
        dom = parseString(data)
        label = dom.getElementsByTagName('v1:strEtiqueta')
        if not label[0].firstChild:
            return False
        return label[0].firstChild.data
