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

import urllib2 # http://www.voidspace.org.uk/python/articles/urllib2.shtml#{{{
import time

import amara
from amara import bindery

from xml.parsers.xmlproc import xmlproc
from xml.parsers.xmlproc import xmlval
from xml.parsers.xmlproc import xmldtd

from pprint import pprint
#}}}

# XML Structure Checking # {{{
class MyApp(xmlproc.Application):
  def handle_start_tag(self,name,attrs):
    pass
  def handle_end_tag(self,name):
    pass
  def handle_data(self,data,start,end):
    pass
  def handle_comment(self,data):
    pass
# }}} 

configXML = bindery.parse('config.xml');
config = configXML.SysInfoRM;

try:
	while (1):
		for host in config.Hosts.host:
			print "Checking %s SysInfo XML" % host.name;
			print host.sysinfourl;
			# TODO: Validate that URL is Valid
			req = urllib2.Request(
				str(host.sysinfourl), 
				{}, 
				{'User-Agent' : str(config.Config.UserAgent), 'Accept' : 'text/xml'}
			);
			sysInfoXML = urllib2.urlopen(req).read();
			p = xmlproc.XMLProcessor();
			p.set_application(MyApp());
			if (str(p.parse_string(sysInfoXML))  == 'None'):
				# TODO: Validate that reutrned data is both XML and valid.
				sysInfo = bindery.parse(sysInfoXML);
				print sysInfo.phpsysinfo.Vitals.IPAddr;
				# Now match against rules and checks in config XML
					
			else:
				sys.stderr.write('Error XML structure invalid');

		time.sleep (30); # This is just for testing final version will monitor timing in another thread
except (KeyboardInterrupt, SystemExit):
	print 'Exiting SysInfoRM';
