import requests
import time
import random
from bs4 import BeautifulSoup

from dokumenty import getDocuments
from oznamenia import getOznamenia

def getDetails(urlDetails:str):
    """Scrapes the specified URL and returns details of zakazka
    
    Parameters
    ----------
    urlDetails : string
        The URL of the Zakazka's details page
        
    Returns
    -------
    dict
       Dictionary containing zakazka data: datumVytvorenia, datumPoslAktualizacie, stav, cpv, druh, datumZverejnenia, dokumenty, oznamenia

    """
    from scraper import WAITING_TIME
    try:
        response = requests.get(urlDetails)
        soup = BeautifulSoup(response.content, 'html.parser')
        detailyZakazky = soup.findAll("tr")
        try:
            datumVytvorenia = detailyZakazky[2].findAll('td')[0].get_text().strip()
            datumPoslAktualizacie = detailyZakazky[3].findAll('td')[0].get_text().strip()            
            stav = list( detailyZakazky[4].findAll('td')[0].stripped_strings)[0].strip()
            cpv = detailyZakazky[5].findAll('td')[0].get_text().strip()
            druh = detailyZakazky[7].findAll('td')[0].get_text().strip()
            datumZverejnenia = detailyZakazky[len(detailyZakazky)-2].findAll('td')[0].get_text().strip()
            print ('DATUM ZVEREJNENIA')
            print (datumZverejnenia)
            if (datumZverejnenia == ''):
                datumZverejnenia = "n/a"
            
            print("random")
            print(random.uniform(0, 1))
            print("random 2")
            print(random.uniform(0, 1))
            time.sleep(WAITING_TIME+ random.uniform(0, 1))
            urlDocuments =  urlDetails.replace('detail', 'dokumenty')
            documents = getDocuments(urlDocuments)

            time.sleep(WAITING_TIME+ random.uniform(0, 1))
            urlOznamenia =  urlDetails.replace('detail', 'oznamenia')
            oznamenia = getOznamenia(urlOznamenia)

            return {
                'datumVytvorenia':datumVytvorenia,
                'datumPoslAktualizacie':datumPoslAktualizacie,
                'stav':stav,
                'cpv':cpv,
                'druh':druh,
                'datumZverejnenia':datumZverejnenia,
                'dokumenty': documents,
                'oznamenia':oznamenia
            }
        except IndexError as e :
            # sometimes the Zakazka details page has a message "Zákazka je momentálne upravovaná" and no data are available
            print('Failed to retrieve details of Zakazka')
            return {
                'datumVytvorenia':'-',
                'datumPoslAktualizacie':'-',
                'stav':'-',
                'cpv':'-',
                'druh':'-',
                'datumZverejnenia':'-',
                'dokumenty': [],
                'oznamenia':[]
            }
    except requests.exceptions.RequestException as e :
        print ('Error in the details request')
        raise e
            
