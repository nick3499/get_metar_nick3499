#! /bin/python3
'''`get_metar_click` module contains `get_decoded_metar()` method
which has four methods bound to it for getting METAR data from airports.
Help doc: python3 get_metar_click.py'''
from subprocess import run
from fire import Fire


def _get_data(icao_code):
    return run(['curl',
                'ftp://tgftp.nws.noaa.gov/data/observations/metar/decoded/' +
                icao_code], check=True)

def mor():
    '''Get decoded METAR for Morris Municipal Airport.'''
    _get_data('KC09.TXT')

def dbq():
    '''Get decoded METAR for Dubuque Regional Airport.'''
    _get_data('KDBQ.TXT')

def dvn():
    '''Get decoded METAR for Davenport Municipal Airport.'''
    _get_data('KDVN.TXT')

def pia():
    '''Get decoded METAR for Peoria International Airport.'''
    _get_data('KPIA.TXT')


if __name__ == '__main__':
    Fire()
