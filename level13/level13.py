#!/usr/bin/python2.6
# -*- coding:utf-8 -*-

import xmlrpclib

url = "http://www.pythonchallenge.com/pc/phonebook.php"
server = xmlrpclib.ServerProxy(url)

# print server.system.listMethods()
# print "phone method  is " , server.system.methodSignature("phone")

print server.phone("Bert")
