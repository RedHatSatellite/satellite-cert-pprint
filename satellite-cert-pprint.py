#!/usr/bin/env python
# File: satellite-cert-pprint.py
# Author: Rich Jerrido <rjerrido@outsidaz.org>
# Purpose: Given a Satellite Entitlement Certificate in XML format
# 'pretty print' it for easier consumption by humans
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

import sys
import os
from optparse import OptionParser
from xml.dom import minidom

parser = OptionParser()
parser.add_option("-f", "--filename", dest="filename", help="path to Satellite Entitlement certificate", metavar="FILENAME")
parser.add_option("--family", dest="family", help="print only channel families that have this string", action="append", default=[])
(options, args) = parser.parse_args()

if not (options.filename):
    print "Must specify a filename.  See usage:"
    parser.print_help()
    print "\nExample usage: ./satellite-cert-pprint.py -h /home/me/redhat.cert"
    sys.exit(1)
else:
    filename = options.filename

if not os.path.isfile(filename):
    print "The specified file : " + filename + " does not appear to exist"
    sys.exit(1)

xmldoc = minidom.parse(filename)
itemlist = xmldoc.getElementsByTagName('rhn-cert-field')
print "=" * 80
print "%-10s%70s" % ("Filename", filename)
if options.family:
    print "%-45s" % "Viewing only channel families listed below"
    for option in options.family:
        print "%s" % option
else:
    print "%-45s" % "Showing all channel families"
print "=" * 80
channel = False
for s in itemlist:
    if s.attributes['name'].value == 'satellite-version':
        print "=" * 80
    if s.attributes['name'].value == 'channel-families':
        if not channel:
            print "=" * 80
            print "%-45s%18s%17s" % ("Channel Family", "Quantity", "Flex")
            print "=" * 80
            channel = True
        try:
            quantity = s.attributes['quantity'].value
        except:
            quantity = 0
        try:
            flex = s.attributes['flex'].value
        except:
            flex = 0
        family = s.attributes['family'].value
        if options.family:
            for option in options.family:
                if option in family:
                    print "%-45s%18s%17s" % (family, quantity, flex)
        else:
            print "%-45s%18s%17s" % (family, quantity, flex)
    else:
        print "%-40s%40s" % (s.attributes['name'].value, s.childNodes[0].nodeValue)

print "=" * 80
