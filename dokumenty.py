import requests
from bs4 import BeautifulSoup

def getDocuments(urlDocuments: str):
    """Scrapes the specified URL and returns a list of documents linked to zakazka

    Parameters
    ----------
    urlDocuments : string
        The URL of the Zakazka's document page

    Returns
    -------
    []
       List of dictionaries containing document info: druhDokumentu, nazovDokumentu, zverejnenie, uprava

    """
    try:
        response = requests.get(urlDocuments)
        soup = BeautifulSoup(response.content, 'html.parser')
        rows = soup.findAll('tr')
        # remove first 3 rows cause it's not the data
        del rows[:3]
        documents = []
        for row in rows:
            cells = row.findAll('td')
            try:
                druhDokumentu = cells[0].get_text().strip()
                nazovDokumentu = cells[1].get_text().strip()
                zverejnenie = cells[len(cells)-2].get_text().strip()
                uprava = cells[len(cells)-1].get_text().strip()
                documents.append({
                    'druhDokumentu': druhDokumentu,
                    'nazovDokumentu': nazovDokumentu,
                    'zverejnenie': zverejnenie,
                    'uprava': uprava
                })
            except IndexError:
                print(f'Error in scraping document details. URL:{
                      urlDocuments}')

        return documents

    except requests.exceptions.RequestException as e:
        print('Error in the Dokumenty request')
        print(e)
        return []
