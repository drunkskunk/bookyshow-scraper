import urllib2
import time
import sys
import smtplib
import urllib
from bs4 import BeautifulSoup
def sendSMS(apikey, numbers, sender, message):
    data =  urllib.urlencode({'apikey': apikey, 'numbers': numbers,
        'message' : message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib2.Request("https://api.textlocal.in/send/?")
    f = urllib2.urlopen(request, data)
    fr = f.read()
    return(fr)
wiki = "https://in.bookmyshow.com/bengaluru/movies/nerkonda-paarvai/ET00104821"
#wiki = "https://in.bookmyshow.com/bengaluru/movies/the-lion-king/ET00089130"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
req=urllib2.Request(wiki,headers=hdr)
while True:
        page = urllib2.urlopen(req)
        soup = BeautifulSoup(page,"lxml")
        for link in soup.find_all("a", class_="showtimes btn _cuatro"):
                if(link.text=="Book Tickets"):
                        resp1 =  sendSMS('BMzyUYzaNDk-BWYH76llh0kJjz1jpmBVbujVjjZBLA', '919066264327','TXTLCL', 'Bookings Open For Nerkonda Paarvai')
                        resp2 =  sendSMS('BMzyUYzaNDk-BWYH76llh0kJjz1jpmBVbujVjjZBLA', '919600902856','TXTLCL', 'Bookings Open For Nerkonda Paarvai')
                        sys.exit()
        time.sleep(3600)
