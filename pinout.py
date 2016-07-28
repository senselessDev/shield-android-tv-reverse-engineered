#! /usr/bin/env python

import numpy

main_pinout_dict = [
    {'J501': 1,
     'desc': 'GND',
     'mainboard': {'row': 7, 'col': 'R'}},
    {'J501': 3,
     'desc': 'RTL8153 USB D+ (Pin 23)',
     'mainboard': {'row': 7, 'col': 'Q'}},
    {'J501': 5,
     'desc': 'RTL8153 USB D- (Pin 22)',
     'mainboard': {'row': 7, 'col': 'P'}},
    {'J501': 7,
     'desc': 'GND',
     'mainboard': {'row': 11, 'col': 'X'}},
    {'J501': 9,
     'desc': 'USB Jack J6 SSRX- (Pin 8)',
     'mainboard': {'row': 11, 'col': 'W'}},
    {'J501': 11,
     'desc': 'USB Jack J6 SSRX+ (Pin 9)',
     'mainboard': {'row': 12, 'col': 'W'}},
    {'J501': 13,
     'desc': 'GND',
     'mainboard': {'row': 12, 'col': 'X'}},
    {'J501': 15,
     'desc': 'USB Jack J5 D- (Pin 2)',
     'mainboard': {'row': 13, 'col': 'X'}},
    {'J501': 17,
     'desc': 'USB Jack J5 D+ (Pin 3)',
     'mainboard': {'row': 13, 'col': 'W'}},
    {'J501': 19,
     'desc': 'GND',
     'mainboard': {'row': 12, 'col': 'S'}},
    {'J501': 21,
     'desc': 'USB Jack J5 SSRX- (Pin 8)',
     'mainboard': {'row': 11, 'col': 'T'}},
    {'J501': 23,
     'desc': 'USB Jack J5 SSRX+ (Pin 9)',
     'mainboard': {'row': 12, 'col': 'T'}},
    {'J501': 25,
     'desc': 'GND',
     'mainboard': {'row': 13, 'col': 'V'}},
    {'J501': 27,
     'desc': 'USB Jack J7 OTG D- (Pin 2)',
     'mainboard': {'row': 12, 'col': 'U'}},
    {'J501': 29,
     'desc': 'USB Jack J7 OTG D+ (Pin 3)',
     'mainboard': {'row': 13, 'col': 'U'}},
    {'J501': 31,
     'desc': 'GND',
     'mainboard': {'row': 6, 'col': 'Q'}},
    {'J501': 33,
     'desc': 'HDMI Jack J3 Data 0 + (Pin 7)',
     'mainboard': {'row': 5, 'col': 'Q'}},
    {'J501': 35,
     'desc': 'HDMI Jack J3 Data 0 - (Pin 9)',
     'mainboard': {'row': 4, 'col': 'Q'}},
    {'J501': 37,
     'desc': 'GND',
     'mainboard': {'row': 4, 'col': 'P'}},
    {'J501': 39,
     'desc': 'HDMI Jack J3 Data 1 + (Pin 4)',
     'mainboard': {'row': 5, 'col': 'P'}},
    {'J501': 41,
     'desc': 'HDMI Jack J3 Data 1 - (Pin 6)',
     'mainboard': {'row': 5, 'col': 'O'}},
    {'J501': 43,
     'desc': 'GND',
     'mainboard': {'row': 6, 'col': 'P'}},
    {'J501': 45,
     'desc': 'HDMI Jack J3 Data 2 + (Pin 1)',
     'mainboard': {'row': 6, 'col': 'O'}},
    {'J501': 47,
     'desc': 'HDMI Jack J3 Data 2 - (Pin 3)',
     'mainboard': {'row': 6, 'col': 'N'}},
    {'J501': 49,
     'desc': 'GND',
     'mainboard': {'row': 5, 'col': 'N'}},
    {'J501': 51,
     'desc': 'HDMI Jack J3 Clock + (Pin 10)',
     'mainboard': {'row': 4, 'col': 'O'}},
    {'J501': 53,
     'desc': 'HDMI Jack J3 Clock - (Pin 12)',
     'mainboard': {'row': 4, 'col': 'N'}},
    {'J501': 55,
     'desc': 'GND',
     'mainboard': {'row': 5, 'col': 'U'}},
    {'J501': 57,
     'desc': 'Voltage ?', #TODO
     'mainboard': {'row': 5, 'col': 'T'}},
    {'J501': 59,
     'desc': 'Voltage ?', #TODO
     'mainboard': {'row': 6, 'col': 'T'}},
    {'J501': 61,
     'desc': 'Voltage ?', #TODO
     'mainboard': {'row': 6, 'col': 'V'}},
    {'J501': 63,
     'desc': '-> Q7 (Pin 2); Q7 (Pin 3) -> J502 (Pin 8) (Levelshifting ?)', #TODO
     'mainboard': {'row': 10, 'col': 'W'}},
    {'J501': 65,
     'desc': '-> Q6 (Pin 2); Q6 (Pin 3) -> J502 (Pin 4) (Levelshifting ?)', #TODO
     'mainboard': {'row': 6, 'col': 'U'}},
    {'J501': 67,
     'desc': 'U4 (Pin 3 and 4) (High Side USB Current Switch?)', #TODO
     'mainboard': {'row': 9, 'col': 'W'}},
    {'J501': 69,
     'desc': 'U5 (Pin 3 and 4) (High Side USB Current Switch?)', #TODO
     'mainboard': {'row': 8, 'col': 'W'}},
    {'J501': 71,
     'desc': 'Q4 (Pin 1) (Levelshifting ?)', #TODO
     'mainboard': {'row': 8, 'col': 'X'}},
    {'J501': 73,
     'desc': 'Q8 (unpopulated) (Levelshifting ?)', #TODO
     'mainboard': {'row': 9, 'col': 'X'}},
    {'J501': 75,
     'desc': 'GND',
     'mainboard': {'row': 8, 'col': 'N'}},
    {'J501': 77,
     'desc': 'USB Jack J6 D- (Pin 2)',
     'mainboard': {'row': 7, 'col': 'N'}},
    {'J501': 79,
     'desc': 'USB Jack J6 D+ (Pin 3)',
     'mainboard': {'row': 7, 'col': 'O'}},

    {'J501': 2,
     'desc': 'GND',
     'mainboard': {'row': 5, 'col': 'X'}},
    {'J501': 4,
     'desc': 'microSD slot RSV/DAT1 (Pin 8)',
     'mainboard': {'row': 4, 'col': 'W'}},
    {'J501': 6,
     'desc': 'microSD slot MISO/DAT0 (Pin 7)',
     'mainboard': {'row': 4, 'col': 'X'}},
    {'J501': 8,
     'desc': 'microSD slot CLK (Pin 5)',
     'mainboard': {'row': 5, 'col': 'W'}},
    {'J501': 10,
     'desc': 'microSD slot MOSI/CMD (Pin 3)',
     'mainboard': {'row': 6, 'col': 'X'}},
    {'J501': 12,
     'desc': 'microSD slot CS/DAT3 (Pin 2)',
     'mainboard': {'row': 5, 'col': 'V'}},
    {'J501': 14,
     'desc': 'microSD slot RSV/DAT2 (Pin 1)',
     'mainboard': {'row': 6, 'col': 'W'}},
    {'J501': 16,
     'desc': 'D502 (open ?)',
     'mainboard': {'row': 7, 'col': 'V'}},
    {'J501': 18,
     'desc': 'GND',
     'mainboard': {'row': 4, 'col': 'V'}},
     {'J501': 20,
      'desc': '-> Q5 (Pin 2); Q5 (Pin 3) -> J502 (Pin 7) (Levelshifting ?)',
     'mainboard': {'row': 11, 'col': 'V'}},
    {'J501': 22,
     'desc': 'U6 Pin 1 (Function ?)',
     'mainboard': {'row': 10, 'col': 'V'}},
    {'J501': 24,
     'desc': 'J502 (Pin 2)',
     'mainboard': {'row': 10, 'col': 'X'}},
    {'J501': 26,
     'desc': 'J7 OTG ID (Pin 4, through diode)',
     'mainboard': {'row': 10, 'col': 'U'}},
    {'J501': 28,
     'desc': 'HDMI Jack J3 CEC (Pin 13)',
     'mainboard': {'row': 6, 'col': 'S'}},
    {'J501': 30,
     'desc': 'HDMI Jack J3 Hot Plug Detect (Pin 19)',
     'mainboard': {'row': 5, 'col': 'S'}},
    {'J501': 32,
     'desc': 'HDMI Jack J3 DDC Data (Pin 16)',
     'mainboard': {'row': 6, 'col': 'R'}},
    {'J501': 34,
     'desc': 'HDMI Jack J3 DDC Clock (Pin 15)',
     'mainboard': {'row': 5, 'col': 'R'}},
    {'J501': 36,
     'desc': 'Power Button J502 (Pin 6)',
     'mainboard': {'row': 11, 'col': 'S'}},
    {'J501': 38,
     'desc': '?', #TODO
     'mainboard': {'row': 12, 'col': 'R'}},
    {'J501': 40,
     'desc': '?', #TODO
     'mainboard': {'row': 12, 'col': 'Q'}},
    {'J501': 42,
     'desc':  '?', #TODO
     'mainboard': {'row': 13, 'col': 'P'}},
    {'J501': 44,
     'desc': 'GND',
     'mainboard': {'row': 11, 'col': 'U'}}, #TODO
    {'J501': 46,
     'desc': 'SATA Jack J504 (Pin 16, AC coupled)',
     'mainboard': {'row': 11, 'col': 'O'}},
    {'J501': 48,
     'desc': 'SATA Jack J504 (Pin 15, AC coupled)',
     'mainboard': {'row': 12, 'col': 'O'}},
    {'J501': 50,
     'desc': 'GND',
     'mainboard': {'row': 11, 'col': 'R'}},
    {'J501': 52,
     'desc': 'SATA Jack J504 (Pin 19, AC coupled)',
     'mainboard': {'row': 12, 'col': 'N'}},
    {'J501': 54,
     'desc': 'SATA Jack J504 (Pin 18, AC coupled)',
     'mainboard': {'row': 13, 'col': 'N'}},
    {'J501': 56,
     'desc': 'GND',
     'mainboard': {'row': 13, 'col': 'O'}},
    {'J501': 58,
     'desc': 'USB Jack J6 SSTX+ (Pin 6, AC coupled)',
     'mainboard': {'row': 11, 'col': 'P'}},
    {'J501': 60,
     'desc': 'USB Jack J6 SSTX- (Pin 5, AC coupled)',
     'mainboard': {'row': 10, 'col': 'P'}},
    {'J501': 62,
     'desc': 'GND',
     'mainboard': {'row': 11, 'col': 'Q'}},
    {'J501': 64,
     'desc': 'USB Jack J5 SSTX+ (Pin 6, AC coupled)',
     'mainboard': {'row': 10, 'col': 'N'}},
    {'J501': 66,
     'desc': 'USB Jack J5 SSTX- (Pin 5, AC coupled)',
     'mainboard': {'row': 10, 'col': 'O'}},
    {'J501': 68,
     'desc': 'GND',
     'mainboard': {'row': 11, 'col': 'N'}},
    {'J501': 70,
     'desc': 'RTL8153 USB SSRX+ (Pin 14)',
     'mainboard': {'row': 9, 'col': 'N'}},
    {'J501': 72,
     'desc': 'RTL8153 USB SSRX- (Pin 15)',
     'mainboard': {'row': 9, 'col': 'O'}},
    {'J501': 74,
     'desc': 'GND',
     'mainboard': {'row': 8, 'col': 'O'}},
    {'J501': 76,
     'desc': 'RTL8153 USB SSTX- (Pin 19)',
     'mainboard': {'row': 8, 'col': 'P'}},
    {'J501': 78,
     'desc': 'RTL8153 USB SSTX+ (Pin 18)',
     'mainboard': {'row': 8, 'col': 'Q'}},
    {'J501': 80,
     'desc': 'GND',
     'mainboard': {'row': 9, 'col': 'P'}},
    # GND pins on mainboard without special J501 pin
    {'J501': 0,
     'desc': 'GND',
     'mainboard': {'row': 7, 'col': 'W'}},
    {'J501': 0,
     'desc': 'GND',
     'mainboard': {'row': 7, 'col': 'X'}},
    {'J501': 0,
     'desc': 'GND',
     'mainboard': {'row': 8, 'col': 'V'}},
    {'J501': 0,
     'desc': 'GND',
     'mainboard': {'row': 9, 'col': 'V'}},
    {'J501': 0,
     'desc': 'GND',
     'mainboard': {'row': 12, 'col': 'V'}}
]

special_pads = [
    {'marking': '*x*',
     'desc': 'non existing pads on mainboard',
     'pads': [
         {'row': 1, 'col': 'E'},
         {'row': 1, 'col': 'F'},
         {'row': 1, 'col': 'G'},
         {'row': 1, 'col': 'R'},
         {'row': 1, 'col': 'S'},
         {'row': 1, 'col': 'T'},
         {'row': 2, 'col': 'E'},
         {'row': 2, 'col': 'F'},
         {'row': 2, 'col': 'G'},
         {'row': 2, 'col': 'R'},
         {'row': 2, 'col': 'S'},
         {'row': 2, 'col': 'T'},
         {'row': 3, 'col': 'E'},
         {'row': 3, 'col': 'F'},
         {'row': 3, 'col': 'G'},
         {'row': 3, 'col': 'R'},
         {'row': 3, 'col': 'S'},
         {'row': 3, 'col': 'T'},
         {'row': 4, 'col': 'E'},
         {'row': 4, 'col': 'F'},
         {'row': 4, 'col': 'G'},
         {'row': 4, 'col': 'R'},
         {'row': 4, 'col': 'S'},
         {'row': 4, 'col': 'T'},
         {'row': 7, 'col': 'F'},
         {'row': 7, 'col': 'G'},
         {'row': 7, 'col': 'H'},
         {'row': 7, 'col': 'S'},
         {'row': 7, 'col': 'T'},
         {'row': 7, 'col': 'U'},
         {'row': 8, 'col': 'E'},
         {'row': 8, 'col': 'F'},
         {'row': 8, 'col': 'G'},
         {'row': 8, 'col': 'H'},
         {'row': 8, 'col': 'R'},
         {'row': 8, 'col': 'S'},
         {'row': 8, 'col': 'T'},
         {'row': 8, 'col': 'U'},
         {'row': 9, 'col': 'E'},
         {'row': 9, 'col': 'F'},
         {'row': 9, 'col': 'G'},
         {'row': 9, 'col': 'H'},
         {'row': 9, 'col': 'R'},
         {'row': 9, 'col': 'S'},
         {'row': 9, 'col': 'T'},
         {'row': 9, 'col': 'U'},
         {'row': 10, 'col': 'F'},
         {'row': 10, 'col': 'G'},
         {'row': 10, 'col': 'S'},
         {'row': 10, 'col': 'T'},
         {'row': 13, 'col': 'E'},
         {'row': 13, 'col': 'F'},
         {'row': 13, 'col': 'G'},
         {'row': 13, 'col': 'R'},
         {'row': 13, 'col': 'S'},
         {'row': 13, 'col': 'T'},
         {'row': 14, 'col': 'E'},
         {'row': 14, 'col': 'F'},
         {'row': 14, 'col': 'G'},
         {'row': 14, 'col': 'R'},
         {'row': 14, 'col': 'S'},
         {'row': 14, 'col': 'T'},
         {'row': 15, 'col': 'E'},
         {'row': 15, 'col': 'F'},
         {'row': 15, 'col': 'G'},
         {'row': 15, 'col': 'R'},
         {'row': 15, 'col': 'S'},
         {'row': 15, 'col': 'T'},
         {'row': 16, 'col': 'E'},
         {'row': 16, 'col': 'F'},
         {'row': 16, 'col': 'G'},
         {'row': 16, 'col': 'R'},
         {'row': 16, 'col': 'S'},
         {'row': 16, 'col': 'T'}
     ]
    },
    {'marking': '*u*',
     'desc': 'no connection on flat flex cable (**u**nconnected)',
     'pads': [
         {'row': 4, 'col': 'U'},
         {'row': 9, 'col': 'Q'},
         {'row': 10, 'col': 'Q'},
         {'row': 12, 'col': 'P'},
         {'row': 13, 'col': 'Q'}
     ]
    },
    {'marking': '*o*',
     'desc': 'pad on mainboard but no spring on connector (**o**pen)',
     'pads': [
          {'row': 10, 'col': 'R'}
     ]
    },
    {'marking': '*g*',
     'desc': '**g**round pads (more on mainboard than pins on J501)',
     'pads': [
         {'row': 4, 'col': 'P'},
         {'row': 4, 'col': 'V'},
         {'row': 5, 'col': 'N'},
         {'row': 5, 'col': 'U'},
         {'row': 5, 'col': 'X'},
         {'row': 6, 'col': 'P'},
         {'row': 6, 'col': 'Q'},
         {'row': 7, 'col': 'R'},
         {'row': 7, 'col': 'W'},
         {'row': 7, 'col': 'X'},
         {'row': 8, 'col': 'N'},
         {'row': 8, 'col': 'O'},
         {'row': 8, 'col': 'V'},
         {'row': 9, 'col': 'P'},
         {'row': 9, 'col': 'V'},
         {'row': 11, 'col': 'N'},
         {'row': 11, 'col': 'Q'},
         {'row': 11, 'col': 'R'},
         {'row': 11, 'col': 'U'},
         {'row': 11, 'col': 'X'},
         {'row': 12, 'col': 'S'},
         {'row': 12, 'col': 'V'},
         {'row': 12, 'col': 'X'},
         {'row': 13, 'col': 'O'},
         {'row': 13, 'col': 'V'}
     ]
    }

]

def table_by_j501_pin(pins, description_dicts):
    table_template = '| {pin_string: <{pin_fill}} | {desc_string: <{desc_fill}} | {mainboard_string: <{mainboard_fill}} |\n'
    pin_string = 'J501 pin'
    desc_string = 'description'
    desc_len = numpy.max([len(pin['desc']) for pin in description_dicts if pin['J501'] in pins])
    mainboard_string = 'mainboard pin'

    result = table_template.format(pin_string = pin_string, pin_fill = len(pin_string),
                                   desc_string = desc_string, desc_fill = desc_len,
                                   mainboard_string = mainboard_string, mainboard_fill = len(mainboard_string))

    result += '| {:} | {:} | {:} |\n'.format('-' * len(pin_string), '-' * desc_len, '-' * len(mainboard_string))

    for i in pins:
        pin_description = [pin for pin in description_dicts if pin['J501'] == i]

        if(len(pin_description) > 1):
            print('pin redefinition for pins {}.'.format([pin['J501'] for pin in pin_description]))
            continue
        if(len(pin_description) < 1):
            print('pin definition for pin {} missing.'.format(i))
            continue

        pin_description = pin_description[0]
        mainboard_pin = '{}{}'.format(pin_description['mainboard']['col'], pin_description['mainboard']['row'])
        result += table_template.format(pin_string = pin_description['J501'], pin_fill = len(pin_string),
                                        desc_string = pin_description['desc'], desc_fill = desc_len,
                                        mainboard_string = mainboard_pin, mainboard_fill = len(mainboard_string))
    return result

def table_by_mainboard_pin(x_start, x_stop, y_start, y_stop, description_dicts, special_pads):
    table_template = '| {: ^{pin_fill}} '

    if(not isinstance(x_start, int)):
        x_start = ord(x_start)
    if(not isinstance(x_stop, int)):
        x_stop = ord(x_stop)

    columns = x_stop - x_start + 2
    column_headers = [chr(i) for i in numpy.arange(x_start, x_stop + 1)]
    result = (table_template * columns).format('      ', *column_headers, pin_fill = 3)
    result += '|\n'
    result += (table_template * columns).format('------', *['-' * 3 for i in range(columns - 1)], pin_fill = 3)
    result += '|\n'

    for y in numpy.arange(y_start, y_stop + 1)[::-1]:
        header = '| **{:}** '.format(y)
        result += '{: <{fill}}'.format(header, fill = 9)
        for x in numpy.arange(x_start, x_stop + 1):
            pin_description = [pin for pin in description_dicts if pin['mainboard'] == {'col': chr(x), 'row': y}]

            if(len(pin_description) > 1):
                print('pin redefinition for pins {}.'.format([pin['J501'] for pin in pin_description]))
                continue

            found = False
            for specialty in special_pads:
                if {'col': chr(x), 'row': y} in specialty['pads']:
                    result += table_template.format(specialty['marking'], pin_fill = 3)
                    found = True
            if not found:
                if len(pin_description) == 1:
                    pin_description = pin_description[0]
                    result += table_template.format(pin_description['J501'], pin_fill = 3)
                else:
                    result += table_template.format('-', pin_fill = 3)
        result += '|\n'

    return result

def images():
    base_url = 'https://senselessdev.github.io/nvidia-shield-tv-pinout/{}.svg'
    images = ['shield_mainboard_connector', 'shield_ioboard_bottom', 'shield_ioboard_top']
    markdown_image_template = '![{}]({})\n\n'

    result = ''

    for image in images:
        result += markdown_image_template.format(image, base_url.format(image))

    return result

def marking_meanings(special_pads):
    table_template = '| {: <{fill}} '

    marking_str = 'marking'
    meaning_str = 'meaning'
    meaning_len = numpy.max([len(specality['desc']) for specality in special_pads])

    result = table_template.format(marking_str, fill = len(marking_str))
    result += table_template.format(meaning_str, fill = meaning_len)
    result += '|\n'

    result += table_template.format('-' * len(marking_str), fill = len(marking_str))
    result += table_template.format('-' * meaning_len, fill = meaning_len)
    result += '|\n'

    for specality in special_pads:
        result += table_template.format(specality['marking'], fill = len(marking_str))
        result += table_template.format(specality['desc'], fill = meaning_len)
        result += '|\n'

    result += '\n\n'

    return result

with open('README.md', 'w') as f:
    f.write('#NVIDIA Shield Android TV - Reverse Engineering\n\n')
    f.write(images())
    f.write('## Sorted by J501 pin number\n\n')
    f.write(table_by_j501_pin(numpy.linspace(1, 79, 40), main_pinout_dict))
    f.write('\n')
    f.write(table_by_j501_pin(numpy.linspace(2, 80, 40), main_pinout_dict))
    f.write('\n')
    f.write('## Sorted by mainboard pad number\n\n')

    f.write(marking_meanings(special_pads))

    f.write(table_by_mainboard_pin('N', 'X', 4, 13, main_pinout_dict, special_pads))
