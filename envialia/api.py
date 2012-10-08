#This file is part of envialia. The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.

from envialia.utils import envialia_url
from envialia.envxml import ENVXML

from xml.dom.minidom import parseString
import urllib2

class API(object):
    """
    Generic API to connect to envialia
    """
    __slots__ = (
        'url',
        'agency',
        'customer',
        'password',
        'session',
        'error',
    )

    def __init__(self, agency, customer, password, debug=False):
        """
        This is the Base API class which other APIs have to subclass. By
        default the inherited classes also get the properties of this
        class which will allow the use of the API with the `with` statement

        Example usage ::

            from envialia.api import API

            with API(agency, customer, password) as envialia_api:
                return envialia_api.test_connection()

        :param agency: API agency of the Envialia Web Services.
        :param customer: API customer of the Envialia Web Services.
        :param password: API password of the Envialia Web Services.
        """
        self.url = envialia_url(debug)
        self.agency = agency
        self.customer = customer
        self.password = password
        self.session = None
        self.error = False

    def __enter__(self):
        """
        Connect to Envialia and get ID session
        """
        envxml = ENVXML()
        data = envxml.envialia_xml_login(self.agency, self.customer, self.password)
        session = self.get_session(data)
        self.session = session
        return self

    def __exit__(self, type, value, traceback):
        """
        Drop ID session
        """
        self.session = None

    def connect(self, data):
        """
        Connect to the Webservices and return XML data from envialia

        :param data: XML data.
        """
        result = urllib2.urlopen(self.url, data)
        data = result.read()
        return data

    def get_session(self, data):
        """
        Connects to the Webservices Service and return Session ID
        (extract from envialia ID session)

        :param data: XML data.
        """
        session = False
        error = False
        faultstring = False

        data = self.connect(data)
        try:
            dom = parseString(data)
            faultstring = dom.getElementsByTagName('faultstring')
            if faultstring:
                error = faultstring[0].firstChild.data
            session = dom.getElementsByTagName('ID')[0].firstChild.data
        except:
            pass

        if faultstring:
            self.error = error
        return session

    def test_connection(self):
        """
        Test connection to Envialia webservices
        """
        return {'session':self.session,'error':self.error}
