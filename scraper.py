import time
import requests
from bs4 import BeautifulSoup
import paster
import random
from collections import OrderedDict

from detailyZakazky import getDetails
from headers import headers_list

# the URL including the CVP filter
URL = 'https://www.uvo.gov.sk/vyhladavanie/vyhladavanie-zakaziek?cpv=48000000-8+72000000-5+73000000-2'
PRE_URL = 'https://www.uvo.gov.sk'

# the amount of time to wait between the requests (in seconds)
WAITING_TIME = 1

def main():
    # starting page number
    pageCounter = 7

    zakazkaCounter = 121

    # ordered_headers_list = []
    # for headers in headers_list:
    #     h = OrderedDict()
    #     for header,value in headers.items():
    #         h[header]=value
    #     ordered_headers_list.append(h)

    while (True):        
        try:
            print ("rewuesting again")
            print (pageCounter)
            print (f'{URL}&page={pageCounter}')
            response = requests.get(f'{URL}&page={pageCounter}', headers=random.choice(headers_list))
            soup = BeautifulSoup(response.content, 'html.parser')

            #get all <tr> tags from the website
            tableRows = soup.findAll("tr")

            # remove the first row cause it contains the table header and not the data              
            tableRows.pop(0)

            for element in tableRows:                
                # get all 'a' tags in each row
                aTags = element.findAll('a')
                # first 'a' tag in each row is the Zakazka
                zakazka = aTags [0]
                titleZakazka = zakazka.get_text().strip()
                urlZakazka = PRE_URL + zakazka['href']
                obstaravatel = aTags[1].get_text().strip()                
                print ("Zakazka")
                print (titleZakazka)
                print ("OBSTARAVATEL")
                print (obstaravatel)
                print (urlZakazka)
                #wait before getting the details because it uses an http request
                time.sleep(WAITING_TIME + random.uniform(0, 1))
                details = getDetails(urlZakazka)                
                zakazkaDict = {
                    'titleZakazka':titleZakazka,
                    'obstaravatel':obstaravatel,
                    'urlZakazka': urlZakazka,
                    'detaily': details
                }
                # the first row in GoogleSheets is used for header therefore zakazkaCounter + 1 
                paster.pasteToGoogleSheets(zakazkaDict, zakazkaCounter+1)
                zakazkaCounter = zakazkaCounter + 1
        
        except requests.exceptions.RequestException as e :        
            raise e
        
        # wait before fetching next page
        time.sleep(WAITING_TIME)
        pageCounter = pageCounter + 1 
        print("Going to next page")
        print(pageCounter)

        # the button linking to the last page is not clickable on the last page - it changes to a span tag, so the findAll('a' returns empty string
        lastPageButton = soup.find_all("a", {"class": "pag-last"})
        print("Last page button")
        print(lastPageButton)
        print("Last page buutton type")
        print(type(lastPageButton))

        if not lastPageButton:
            print('Bottom of last page reached. Exiting')
            break
        else:
            continue

if __name__ == '__main__':
    main()
