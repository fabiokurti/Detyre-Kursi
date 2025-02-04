import pandas as pd

# Leximi i të dhënave nga web scraping
scraped_data = pd.read_csv('data.csv')

# Leximi i të dhënave nga API
with open('weather_data.json', 'r') as file
    weather_data = json.load(file)

# Shtimi i të dhënave nga API në DataFrame
scraped_data['Weather'] = weather_data['weather'][0]['description']

# Ruajtja e të dhënave të bashkuara
scraped_data.to_csv('final_data.csv', index=False)