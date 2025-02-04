import requests
from bs4 import BeautifulSoup
import csv

# URL e faqes
url = "https://www.bbc.com/news"

# Kërkesa HTTP për të marrë HTML-n e faqes
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Nxjerrja e titujve të artikujve
titles = soup.find_all('h3')  # Ndryshoni në bazë të strukturës së faqes

# Ruajtja e të dhënave në një skedar CSV
with open('data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title'])  # Header
    for title in titles:
        writer.writerow([title.get_text()])