print("this will fetch result in the excel data.")

import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the webpage
url = "http://127.0.0.1:5500/AKTU%20One%20View%20By%20AKTU%20SDC.html"  # Replace with the actual URL of the website

# Send an HTTP GET request to the URL
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the table with the specified ID
    table = soup.find("table", {"id": "ctl04_ctl00_ctl00_grdViewSubjectMarksheet"})

    if table:
        # Use Pandas to read the table into a DataFrame
        df = pd.read_html(str(table))[0]  # Use [0] as there may be multiple tables on the page

        # Export the DataFrame to an Excel file
        df.to_excel("output.xlsx", index=False)
        print("Table data exported to 'output.xlsx'")
    else:
        print("Table with the specified ID not found on the page.")
else:
    print("Failed to fetch the webpage.")
