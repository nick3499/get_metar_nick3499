#! /bin/python3
'''`get_metar` module contains `decode_metar()` method which receives
CSV data and extracts a specific row of weather data.'''
import dateutil.parser


def decode_metar():
    '''`get_metar()` method extracts/prints METAR data from CSV record.'''
    blue = '\033[1;34m'  # format text blue
    reset = '\033[0m'  # reset text format
    file_obj = open('data.txt', 'r')  # file object
    read_file = file_obj.read().split(',')  # list of strings 
    parse_date = dateutil.parser.parse(read_file[2])  # format date
    # for conversion of wind direction angle
    wind_dir = {
        '350': 'N', '360': 'N', '010': 'N',
        '20': 'N/NE', '30': 'N/NE',
        '40': 'NE', '50': 'NE',
        '60': 'E/NE', '70': 'E/NE',
        '80': 'E', '90': 'E', '100': 'E',
        '110': 'E/SE', '120': 'E/SE',
        '130': 'SE', '140': 'SE',
        '150': 'S/SE', '160': 'S/SE',
        '170': 'S', '180': 'S', '190': 'S',
        '200': 'S/SW', '210': 'S/SW',
        '220': 'SW', '230': 'SW',
        '240': 'W/SW', '250': 'W/SW',
        '260': 'W', '270': 'W', '280': 'W',
        '290': 'W/NW', '300': 'W/NW',
        '310': 'NW', '320': 'NW',
        '330': 'N/NW', '340': 'N/NW'}
    print(f'{blue}ICAO Airport Code:{reset:<5}{read_file[1]}')
    print(f'{blue}Latitude/Longitude:{reset:<4}{read_file[3]}  {read_file[4]}')
    print(f'{blue}Observation Time:{reset:<6}{parse_date.strftime("%m/%d/%Y, %H:%M:%S")} UTC')
    print(f'{blue}Temperature:{reset:<11}{(float(read_file[5]) * 9/5) + 32:0.1f}°F  {read_file[5]}°C')
    print(f'{blue}Dewpoint:{reset:<14}{(float(read_file[6]) * 9/5) + 32:0.1f}°F  {read_file[6]}°C')
    print(f'{blue}Wind Direction:{reset:<8}{wind_dir[read_file[7]]}  {read_file[7]}°')
    print(f'{blue}Wind Speed Knots:{reset:<6}{read_file[8]} knots')
    print(f'{blue}Visibility:{reset:<12}{read_file[10]} statute miles')
    print(f'{blue}Altimeter:{reset:<13}{float(read_file[11]):0.2f} Hg')
    print(f'{blue}Sky Condition:{reset:<9}{read_file[22]}')
    print(f'{blue}Elevation (meters):{reset:<4}{read_file[43]}')


if __name__ == '__main__':
    decode_metar()  # if standalone, run app
