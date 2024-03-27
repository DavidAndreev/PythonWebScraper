# Python Web Scraper

Scrapes the website of https://www.uvo.gov.sk/ for the orders with given filter and pastes this data into Google Sheets Document.

## Usage

First, create your Google Cloud API key as json file and paste it in the project folder.
Then link to this file in the ```paster .py ``` on the following line:

```py
# Google Cloud API key file
SERVICE_KEY_PATH = 'your-api-key-json-file.json'
```

Find the ID of your Google Sheet Document (in the URL for example) and paste in the following line of the ```paster .py ```

```py
# ID of the GoogleSheet document - needs to be permitted to edit by anyone
SPREADSHEET_ID = 'your-sheet-id-goes-here' 
```

Make sure that anyone with the link to the Google Sheet can edit the sheet.

Then you're ready to install the dependencies and run the program:

Change directory to the project folder
```bash
cd folder-name 
```
Install the dependencies from the ```requirements .txt ``` file

```bash
pip install -r requirements.txt
```

Run the  ```scraper .py ```

```bash
python scraper.py
```

Enjoy!