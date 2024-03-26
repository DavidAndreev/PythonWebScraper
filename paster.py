from utility import dokumentyToString, oznameniaToString
import gspread

# Google Cloud API key file
SERVICE_KEY_PATH = 'pythonscraper-418308-f3f4031afefe.json'
gc = gspread.service_account(SERVICE_KEY_PATH) 

# ID of the GoogleSheet document - needs to be permitted to edit by anyone
SPREADSHEET_ID = '1t52nJm47J_vT-9wpiNJfvOSrO-Di0zaWI-7hI5W-rzk' 
WORKSHEET_NAME = 'Sheet2'

def pasteToGoogleSheets(zakazka:dict, row:int):
    """Inserts the contents of zakazka dictionary into Google Sheets on the specified row
    
    Parameters
    ----------
    zakazka : dict
        Dictionary with zakazka data
    row : int
        Number of the row to paste the data in

    """
    wb = gc.open_by_key(SPREADSHEET_ID)
    workSheet = wb.worksheet(WORKSHEET_NAME)
    print(zakazka["titleZakazka"])
    print(zakazka["obstaravatel"])
    print (type(zakazka["titleZakazka"]))
    print (type(zakazka["obstaravatel"]))
    print (type(zakazka))
    workSheet.update('A1', [["URL",  "Názov", 'Obstarávateľ', 'Dátum vytvorenia', 'Dátum poslednej aktualizácie', 
                       'Stav', 'CPV', 'Druh', 'Dátum zverejnenia', 'Dokumenty', 'Oznámenia' ],[]]) 
    workSheet.update(f'A{row}', [[zakazka["urlZakazka"], zakazka["titleZakazka"], zakazka["obstaravatel"], 
                                    zakazka["detaily"]["datumVytvorenia"],
                                    zakazka["detaily"]["datumPoslAktualizacie"],
                                    zakazka["detaily"]["stav"],
                                    zakazka["detaily"]["cpv"],
                                    zakazka["detaily"]["druh"],
                                    zakazka["detaily"]["datumZverejnenia"],
                                    dokumentyToString(zakazka["detaily"]["dokumenty"],),
                                    oznameniaToString(zakazka["detaily"]["oznamenia"])                             
                                     ],[]]) 