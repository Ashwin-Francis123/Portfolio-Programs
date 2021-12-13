from bs4 import BeautifulSoup
import requests

currency = input("Currency: ").lower().replace(" ","-")

url = f"https://coinmarketcap.com/currencies/{currency}/"

html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "html.parser")
try:
    Stock_Price = soup.find_all('span')[28].text
    print(currency.capitalize() + " Price: " + Stock_Price)
except IndexError:
    print("Please use a valid currency")
    
