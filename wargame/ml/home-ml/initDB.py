#!/usr/bin/env python
# coding: UTF-8
#    DB init script
#    Copyright (C) 2013  Martin Dubé
#    Version: 2013-10-20:2020
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#import shelve
#d = shelve.open(filename) # open -- file may get suffix added by low-level
#                          # library
#d[key] = data   # store data at key (overwrites old data if
#                # using an existing key)
#data = d[key]   # retrieve a COPY of data at key (raise KeyError if no
#                # such key)
#del d[key]      # delete data stored at key (raises KeyError
#                # if no such key)
#flag = d.has_key(key)   # true if the key exists
#klist = d.keys() # a list of all existing keys (slow!)
#
## as d was opened WITHOUT writeback=True, beware:
#d['xx'] = range(4)  # this works as expected, but...
#d['xx'].append(5)   # *this doesn't!* -- d['xx'] is STILL range(4)!
#
## having opened d without writeback=True, you need to code carefully:
#temp = d['xx']      # extracts the copy
#temp.append(5)      # mutates the copy
#d['xx'] = temp      # stores the copy right back, to persist it
#
## or, d=shelve.open(filename,writeback=True) would let you just code
## d['xx'].append(5) and have it work as expected, BUT it would also
## consume more memory and make the d.close() operation slower.
#
#d.close()       # close it

# clear log file
open('/root/logs/buildingSensor.log', 'w').close()

import shelve

dbFile = '/home/ml/missile2k13.shelve'
d = shelve.open(dbFile, writeback=True)

# secure modules
d['secureMods'] = {}
d['secureMods']['fire'] = {'description': 'This module let the country fire a missile', 'key': 'DPQJDUEja43H8Dfhmjaq', 'locked': True}

# Last launches
d['launches'] = []
#d['launches'].append({'mlId': None, 'source': None, 'datetime': None, 'crashed': None})       # Only for structure example

# Set remaining missiles
d['remainingMissiles'] = [4, 4, 4]

# Set remaining building
d['buildings'] = []
d['buildings'].append({'name': 'Grate ciel', 'value': 3, 'crashed': False, 'flag': 'GngWo2MipVoLTIhID7eJ'})
d['buildings'].append({'name': 'something', 'value': 5, 'crashed': False, 'flag': 'sACGbNlemvcMXX9K2sD6'})

# Login flag
d['loginFlag'] = 'K5ycRDu478mLQTZnTiYX'

# Given flags list
d['flagsGiven'] = []

# Light Status (False = Off, True = On)
d['lightStatus'] = False

d.sync()
d.close()
