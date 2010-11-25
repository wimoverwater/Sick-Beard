import sickbeard
import random
import cookielib
import urllib
import urllib2
import re

from lib.BeautifulSoup import BeautifulSoup
from sickbeard import logger

USERAGENT = random.choice(("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 5.1; .NET CLR 1.1.4322)",
    "Opera/9.20 (Windows NT 6.0; U; en)"))
	
def doLogin(username, password):
    logger.log(u"Contacting MyEpisodes.com", logger.DEBUG)
	
    try:
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        url = "http://www.myepisodes.com/login.php"
        data = urllib.urlencode({"username":username, "password":password, "u":"views.php", "action":"Login", "User-Agent":USERAGENT})
        soup = BeautifulSoup(opener.open(url, data))
        loggedInAs = soup.strong.string
        response = 'Succesfully logged in to MyEpisodes.com as ' + loggedInAs
        logger.log(u"response: " + response, logger.DEBUG)
    except:
        response = 'Could not login to MyEpisodes.com'
        logger.log(u"Warning: " + response)

    return response
	
def notifyMyepisodes(type, message):
    if not sickbeard.USE_MYEPISODES:
        return False

    doLogin(sickbeard.MYEPISODES_USERNAME, sickbeard.MYEPISODES_PASSWORD)
    msg = str(type) + " of " + message
    return msg