from pushsafer import init, Client
from bs4 import BeautifulSoup
import requests
import time

init("n6mZNyt5TalDLqYtAU5m")
patrickIphoneId = '16866'
elliottIphoneId = '16869'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
url = 'https://glastonbury.seetickets.com/content/extras'
url2 = 'https://imgur.com/vn2Mskc'
textPattern = '"All Glastonbury 2019 tickets have now sold out."'

while True:
    response = requests.get(url2, headers=headers)
    soup = BeautifulSoup(response.text, features="html.parser")
    if str(soup).find(textPattern) == -1:
        Client("").send_message("The Glastonbury website has changed. Tap to visit", "Glastonbury tracker", elliottIphoneId,
                                "2", "0", "2",
                                "https://glastonbury.seetickets.com/content/extras", "Open seetickets",
                                "0", "", "", "", "", "", "", "")
        time.sleep(600)
    else:
        time.sleep(5)


