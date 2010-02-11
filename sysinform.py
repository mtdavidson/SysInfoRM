#!/usr/bin/python
###############################################################################
#
# SysInfoRM - System Information Remote Monitoring
#
###############################################################################
#
# TODO: Set License
# TODO: Use assertions and other error handling.
# TODO: Introduce methods and classes.

import urllib2 # http://www.voidspace.org.uk/python/articles/urllib2.shtml
import time

import amara
from amara import bindery

configXML = bindery.parse('config.xml');
config = configXML.SysInfoRM;

while (1):
	for host in config.Hosts.host:
		print "Importing %s XML" % host.name;
		print host.sysinfourl;
		# TODO: Validate that URL is Valid
		req = urllib2.Request(str(host.sysinfourl), {}, {'User-Agent' : str(config.Config.UserAgent), 'Accept' : 'text/xml'});
		sysInfoXML = urllib2.urlopen(req);
		# TODO: Validate that reutrned data is both XML and valid.
		print len(sysInfoXML.read());	
	
	time.sleep (20); # This is just for testing final version will monitor timing in another thread
