# This program knows about the frequencies of various FM radio stations in
# London.
#
# Usage:
#
# $ python radio_freq.py [station_name]
#
# For instance:
#
# $ python radio_freq.py "Radio 4"
# You can listen to Radio 4 on 92.5 FM
#
# or:
#
# $ python radio_freq.py "BBC Radio 5"
# I don't know the frequency of BBC Radio 5

import argparse

fm_frequencies = {
    '89.1 MHz': 'BBC Radio 2',
    '91.3 MHz': 'BBC Radio 3',
    '93.5 MHz': 'BBC Radio 4',
    '94.9 MHz': 'BBC London',
    '95.8 MHz': 'Capital FM',
    '97.3 MHz': 'LBC',
    '98.8 MHz': 'BBC Radio 1',
    '100.0 MHz': 'Kiss FM',
    '100.9 MHz': 'Classic FM',
    '105.4 MHz': 'Magic',
    '105.8 MHz': 'Virgin',
    '106.2 MHz': 'Heart 106.2',
}

description = 'This program knows the frequencies of various FM radio stations in London.'
'I know about {} FM radio stations'.format(len(fm_frequencies))

# TODO:
# * Implement the program as described in the comments at the top of the file.

# 1. Describe the expected command line argument using argparse
parser = argparse.ArgumentParser(description=description)
parser.add_argument("radio_station", type=str, help="Gets frequency for radio station")
args = parser.parse_args() 

# 2. Write function to extract data from dict
def get_frequency(): 
    result = [key for key, value in fm_frequencies.items() if value == args.radio_station]

    if result:
        return f"You can listen to {args.radio_station} on {''.join(result)}"       
    else:
        list = [v for v in fm_frequencies.values()]
        stations = '\n'.join(list)
        return f"I don't know the frequency of {args.radio_station}, but here is a list of the {len(fm_frequencies)} stations I know about: \n \n{stations}"
        
output = get_frequency()
print(output)

# TODO (extra):
# * Change the program so that if the radio station is not found, the user is
#   given a list of all stations that the program does know about.
# * Change the program so that if it is called without arguments, a table of
#   all radio stations and their frequencies is displayed.
