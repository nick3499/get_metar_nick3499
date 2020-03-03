#! /bin/python3
'''`get_metar` module contains `decode_metar()` method which receives
CSV data and extracts a specific row of weather data.'''
from csv import reader
import dateutil.parser
# from subprocess import run

def decode_metar():
    '''`get_metar()` method extracts/prints METAR data from CSV record.'''
    blue = '\033[1;34m'
    reset = '\033[0m'
    with open('data.csv', 'r') as _file:
        _reader = reader(_file)
        for row in _reader:
            # replace `KC09` with preferred ICAO airport code
            if row[0][:4] == 'KC09':
                _parse = dateutil.parser.parse(row[2])
                print(f'{blue}ICAO Airport Code:{reset:<11} {row[1]}')
                print(f'{blue}Observation Time:{reset:<12} {_parse.strftime("%m/%d/%Y, %H:%M:%S")} UTC')
                print(f'{blue}Latitude:{reset:<20} {row[3]}')
                print(f'{blue}Longitude:{reset:<19} {row[4]}')
                print(f'{blue}Temperature Celcius:{reset:<9} {row[5]}')
                print(f'{blue}Dewpoint Celcius:{reset:<12} {row[6]}')
                print(f'{blue}Wind Direction Degrees:{reset:<6} {row[7]}')
                print(f'{blue}Wind Speed Knots:{reset:<12} {row[8]}')
                print(f'{blue}Visibility Statute Miles:{reset:<3} {row[10]}')
                print(f'{blue}Altimeter Hg:{reset:<16} {row[11]}')
                print(f'{blue}Sky Condition:{reset:<15} {row[22]}')
                print(f'{blue}Elevation Metric:{reset:<12} {row[43]}')


if __name__ == '__main__':
    decode_metar()  # if standalone, run app
