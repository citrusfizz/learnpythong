import urllib
import re
Symbols = ["bbry","aapl","spy","goog","nflx"]


for i in Symbols:
    u = "http://finance.yahoo.com/q?s=" + i
    htmlfile = urllib.urlopen(u)
    htmltext = htmlfile.read()
    regex = '<span id="yfs_l84_'+i+'">(.+?)</span>'
    pattern = re.compile(regex)
    price = re.findall(pattern,htmltext)
    print "Ticker: " + str(i) + " is " + str(price)
