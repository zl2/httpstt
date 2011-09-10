import sys
import os
import codecs

#Direct web api use not implemented yet.
def parse(filename):
    os.chdir("data")
    try:
        indata=open(filename).read()
    except:
        print "Error opening file "+filename+"."
        return False
    if "WEATHER" in indata:
        #send weather data
        import getrss
        os.chdir("..") #Needed to get the file city
        outdata=getrss.getweather()
        os.chdir("data")
        outf=codecs.open("weatherrss","w","utf-8")
        print >>outf,outdata
        outf.close()
        os.system("espeak -f weatherrss -s 110 -w sttout.wav")
    elif "RADIO" in indata:
        #stream radio
        os.system('espeak "Radio not yet implemented" -s 100 -w sttout.wav')
        pass
    elif "TIME" in indata:
        #give current time
        os.system("date +%I:%M\ %p | espeak -w sttout.wav")
    elif "FORTUNE" in indata:
        #call fortune
        os.system("/usr/games/fortune > lastfortune")
        os.system("espeak -f lastfortune -s 130 -w sttout.wav")
    else:
        #return error message
        os.system('espeak "I did not understand" -s 100 -w sttout.wav')
    os.system("lame sttout.wav sttout.mp3")
    os.chdir("..")
    print '<a href="data/sttout.mp3">Answer</a>'

if __name__=="__main__":
    if len(sys.argv)<=1:
        print "Usage..."
        sys.exit(0)
    else:
        parse(sys.argv[1])
