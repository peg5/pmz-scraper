#! python3

import requests
import bs4
import csv

URL = 'http://www.progmetalzone.com/category/new-releases/'
new_release_links = []
artist = []

response = requests.get(URL)
response.raise_for_status()
soup = bs4.BeautifulSoup(response.text, "html.parser")
new_release_links = [a.attrs.get('href') for a in soup.select('h2.entry-title a')]

for i in range(len(new_release_links)):
    response = requests.get(new_release_links[i])
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    artist = soup.select('tr td.column-1')
    for j in range(len(artist)):
        artist_name = []
        artist_name.append(artist[j].get_text())
        bands = open('bands.csv', "a", newline="")
        bandsWriter = csv.writer(bands)
        bandsWriter.writerow(artist_name)
        del artist_name

bands.close()

print('Bands written to CSV file.')
