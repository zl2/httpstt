import os

def parse(filename):
    os.chdir("data")
    try:
        indata=open(filename).read()
    except:
        print "Error opening file "+filename+"."
        return False
    #Could do actual parsing here instead.
    print "You said:<br><b>"
    print indata
    print "</b>"
    return True
