from bs4 import BeautifulSoup
import requests
from urllib.parse import quote

def scrape_for_images(chord_name):
    # web scraper service
    chords = []
    request_url = "https://www.scales-chords.com/chord/guitar/" + quote(chord_name)
    html_text = requests.get(request_url).text  # get html text from site
    soup = BeautifulSoup(html_text, 'lxml') # parse site
    div = soup.find_all('div', style = 'margin: 0 auto;text-align:center;')

    if not div:
        return None

    for img in div:
        chord = img.find('img')
        chord = chord['src']    #get img src
        chord = 'https://www.scales-chords.com' + chord
        chords.append({'link': chord})

    return chords # list of dicts of chord img links