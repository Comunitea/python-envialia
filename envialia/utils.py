#This file is part of envialia. The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.

def envialia_url(debug=False):
    """
    Envialia URL connection

    :param debug: If set to true, use Envialia test URL
    """
    if debug:
        return 'http://wstest.envialia-urgente.com:9082/soap'
    else:
        return 'http://wstest.envialia-urgente.com:9082/soap' #TODO: Change this URL to production


