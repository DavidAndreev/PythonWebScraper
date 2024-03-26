import requests
import time
from bs4 import BeautifulSoup

def getOznamenia(urlOznamenia:str):
    """Scrapes the specified URL and returns a list of oznamenia linked to zakazka
    
    Parameters
    ----------
    urlOznamenia : string
        The URL of the zakazka's oznamenia page
        
    Returns
    -------
    []
       List of dictionaries containing oznamenie data: skratka, datumZverejnenia, urlOznamenie
    
    """


    from scraper import PRE_URL

    try:
        response = requests.get(urlOznamenia)
        soup = BeautifulSoup(response.content, 'html.parser')
        rows = soup.findAll("tr")
        del rows [:3]
        oznamenia = []
        for row in rows:
            cells =  row.findAll('td')
            try:
                # get the skratka from the cell containing the title        
                titleStrings = list(cells[0].stripped_strings)
                firstTitleString = titleStrings[0]
                skratka = firstTitleString[len(firstTitleString)-3:]

                datumZverejnenia = cells[1].get_text().strip()
                print (datumZverejnenia)
                onclick = row['onclick']
                urlOznamenie = PRE_URL + onclick[onclick.index("'")+1:-1]
                oznamenia.append({
                    'skratka':skratka,
                    'datumZverejnenia':datumZverejnenia,
                    'urlOznamenie':urlOznamenie
                })
            except IndexError:
                print(f'Error in scraping oznamenie details. URL:{
                      urlOznamenia}')
        
        return oznamenia
    
    except requests.exceptions.RequestException as e :
        print ('Error in the Oznamenia request')
        print (e)
        return []

