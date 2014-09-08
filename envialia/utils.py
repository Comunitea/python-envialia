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
        return 'http://ws.envialia-urgente.com/soap'


def services():
    services = {
        '10': 'Entrega antes de las 10h',
        '100': 'INT-COURIER',
        '101': 'INT-BAG',
        '14': 'Entrega antes de las 13h',
        '200': 'EU-ESTANDAR',
        '24': 'Entrega antes de las 19',
        '300': 'EU-PACK',
        '301': 'EU-BAG',
        '72': 'Entrega antes de 72h',
        '830': 'Entrega antes de las 8:30',
        'CM': 'Canarias Maritimo',
        'DEV': 'Devolucion',
        'E24': 'ECOMM 24 Entrega dia siguiente',
        'E72': 'ECOMM 72 Entrega en tres dias',
        'EEU': 'ECOMM Europe Express',
        'EWW': 'ECOMM Worldwide',
        'RCS': 'Retorno copia sellada',
        'RED': 'Recogeran en delegacion',
        'RET': 'Retorno',
        'SMD': 'Servicio Medio Dia',
        'V00': 'Valija Todo Dia',
        'V10': 'Valija 10h',
        'V14': 'Valija 14h',
    }
    return services

def status_codes():
    return {
        '0': 'Documentado',
        '1': 'En transito',
        '2': 'En reparto',
        '3': 'Incidencia',
        '4': 'Entregado',
    }