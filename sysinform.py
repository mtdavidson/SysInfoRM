#!/usr/bin/python

import urllib2
import libxml2

from elementtree.ElementTree import parse, XML, fromstring, tostring

file = open('config.xml', "r");
tree = parse(file);

for host in tree.findall("//Hosts/host"):
  print host.get('group');
