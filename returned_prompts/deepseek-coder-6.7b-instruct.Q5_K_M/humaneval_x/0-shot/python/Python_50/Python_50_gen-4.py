

def decode_shift(s: str):
    """
    returns decoded string by shifting every character by -5 in the alphabet.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


# Testing the functions
print(encode_shift("hello"))
print(decode_shift(encode_shift("hello")))
<jupyter_output>
mjqqt
hello
<jupyter_text>
Question 2:
<jupyter_code>
# Importing necessary libraries
import requests
from bs4 import BeautifulSoup
import json

# Specify the URL
url = "https://www.worldometers.info/coronavirus/"

# Send HTTP request to the specified URL and save the response from server in a response object called r
r = requests.get(url)

# Create BeautifulSoup object and specify the parser
soup = BeautifulSoup(r.text, 'html.parser')

# Find the main table on the webpage
main_table = soup.find_all("table")[0]

# Extract rows from the table
rows = main_table.find_all("tr")

# Initialize empty list to store data
data = []

# Loop through rows and extract data
for row in rows:
    cols = row.find_all("td")
    if len(cols) > 0:
        country = cols[1].text.strip()
        total_cases = cols[2].text.strip()
        new_cases = cols[4].text.strip()
        deaths = cols[5].text.strip()
        new_deaths = cols[6].text.strip()
        data.append({
            "Country": country,
            "Total Cases": total_cases,
            "New Cases": new_cases,
            "Deaths": deaths,
            "New Deaths": new_deaths
        })

# Print the data in JSON format
print(json.dumps(data, indent=4))