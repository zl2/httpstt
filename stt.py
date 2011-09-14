#!/usr/bin/env python

import cgi
import os
import cgitb
import sys
from parseoutput import parse

LIMIT=10
form = cgi.FieldStorage()
print "Content-Type: text/html; charset=utf-8\r\n"
print "\r\n"
print """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html>
<body>
"""

def getfile(fieldname,filename):
    if fieldname not in form:
        print "Error reading file.<br>"
        return False
    fileitem = form[fieldname]
    if not fileitem.file: 
        print "Error reading file.<br>"
        return False
    f = file(filename, 'wb')
    size=0
    while 1:
        chunk = fileitem.file.read(100000)
        if not chunk: break
        f.write(chunk)
        size+=1
        if size>LIMIT:
            print "Error: File too large."
            return False
    f.close()
    return True

datadir = open("sttconfig").readline().strip()
inputfile = os.path.join(datadir,"input.wav")
#could use a variable filename for archiving
if "skipget" in form or getfile("file",inputfile):
    print "File successfully obtained.<br>"
    sys.stdout.flush()
    errorcode=os.system("./convertone "+inputfile)

    parse("output.hyp")
print """</body>
</html>
"""
