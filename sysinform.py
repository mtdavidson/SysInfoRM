#!/usr/bin/python
###############################################################################
#
# SysInfoRM - System Information Remote Monitoring
#
###############################################################################
#
# TODO: Set License
# TODO: User assertions and other error handling.
# TODO: Introduce methods and classes.

import urllib2
import time

import amara
from amara import bindery

configXML = bindery.parse('config.xml');
config = configXML.SysInfoRM;

for host in config.Hosts.host:
	print "Importing %s XML" % host.name;
	print host.sysinfourl;
	# TODO: Validate that URL is Valid
	sysInfoXML = urllib2.urlopen(str(host.sysinfourl)); # TODO: Need to expand on this to make valid for mod_security
	# TODO: Validate that reutrned data is both XML and valid.
	print len(sysInfoXML.read());	
	time.sleep (20);
