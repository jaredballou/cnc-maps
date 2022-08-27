#!/usr/bin/env python3

import configparser
import fnmatch
import glob
import os
import re

def findfiles(which, where='.'):
    '''Returns list of filenames from `where` path matched by 'which'
       shell pattern. Matching is case-insensitive.'''
    # TODO: recursive param with walk() filtering
    rule = re.compile(fnmatch.translate(which), re.IGNORECASE)
    return [name for name in os.listdir(where) if rule.match(name)]


config = configparser.ConfigParser()

for map in findfiles('*.ini'):
    print(map)
    mapdata = config.read(map)
    print(mapdata)
    jsonpath = os.path.splitext(map)[0] + ".JSON"
    print(jsonpath)