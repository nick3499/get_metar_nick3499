#! /bin/python3
'''`get_decoded_metar` module contains `get_decoded_metar()` method
which returns decoded METAR data. METARs: KC09, KDBQ, KDVN, KPIA
$ python3 get_metar.py --help'''
from subprocess import run
import click


def _get_data(icao_code):
    return run(['curl',
                'ftp://tgftp.nws.noaa.gov/data/observations/metar/decoded/' +
                icao_code], check=True)

@click.group()
@click.option('--station/--no-station', default=False)
def get_decoded_metar(station):
    '''`decoded_metar()` returns decoded METAR data.\n'''

@get_decoded_metar.command()
def mor():
    '''Get decoded METAR data for Morris Municipal Airport.'''
    _get_data('KC09.TXT')

@get_decoded_metar.command()
def dbq():
    '''Get decoded METAR data for Dubuque Regional Airport.'''
    _get_data('KDBQ.TXT')

@get_decoded_metar.command()
def dvn():
    '''Get decoded METAR data for Davenport Municipal Airport.'''
    _get_data('KDVN.TXT')

@get_decoded_metar.command()
def pia():
    '''Get decoded METAR data for Peoria International Airport.'''
    _get_data('KPIA.TXT')


if __name__ == '__main__':
    get_decoded_metar()  # if standalone, run app
