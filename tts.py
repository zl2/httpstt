#!/usr/bin/env python

import cgi
import os
import cgitb

form = cgi.FieldStorage()
print "Content-Type: text/html; charset=utf-8\r\n"
print "\r\n"
print """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html>
<body>
"""

if "text" not in form:
    print "Error, missing 'text' parameter"
    sys.exit(0)
else:
    text=form["text"].value
if "voice" not in form:
    voice="en"
else:
    voice=form["voice"].value
if "speed" is not form:
    speed="110"
else:
    speed=form["speed"].value
#print 'espeak -w data/out.wav -v '+voice+' -s '+speed+' "'+text+'"'
os.system('espeak -w data/out.wav -v '+voice+' -s '+speed+' "'+text+'"')
os.system('lame data/out.wav data/out.mp3')
print "<a href='data/out.mp3'>Answer</a>"
print """</body>
</html>
"""
