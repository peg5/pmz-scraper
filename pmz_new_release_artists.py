#! /usr/bin/python3

#    pmz_new_release_artists.py
#    Copyright (C) 2015  Patrick Graham
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import requests
import bs4
import csv

URL = 'http://www.progmetalzone.com/category/new-releases/'
new_release_links = []
artist = []
bands = open('bands.csv', "a", newline="")

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
        bandsWriter = csv.writer(bands)
        bandsWriter.writerow(artist_name)
        del artist_name

bands.close()

print('Bands written to CSV file.')
