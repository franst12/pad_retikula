import requests
from bs4 import BeautifulSoup
import json

def scrape_and_generate_api():
    url = "https://example-sumber-terbuka.com/crosshairs"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    reticle_urls = []
    
    for img in soup.find_all('img', class_='reticle-icon'):
        reticle_urls.append(img['src'])
        
    with open('reticles_api.json', 'w') as f:
        json.dump({"data": reticle_urls}, f)

if __name__ == "__main__":
    scrape_and_generate_api()