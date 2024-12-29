#importing libraries required
import requests
from bs4 import BeautifulSoup
import csv

#getting url from the user
url = input("Enter URL :")
response = requests.get(url)

#checking if response requested is being fetched or not
if response.status_code == 200:
    print("WebPage Fetched!!!")
else:
    print("WebPage Not Found!!!")

#parsing webpage
soup = BeautifulSoup(response.text, "html.parser")

data = []
links = soup.find_all('a')

for link in links:
    href = link.get('href')
    text = link.text.strip()
    if href:
        data.append([text,href])

# saving file in the form of csv file
csv_filename = "scraped_data.csv"
with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["Link Text", "URL"])
    # Write the data
    writer.writerows(data)

print(f"Data successfully saved to {csv_filename}!")

