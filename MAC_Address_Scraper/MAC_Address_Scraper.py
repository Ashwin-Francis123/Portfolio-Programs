import optparse
import re
from bs4 import BeautifulSoup
import requests

def MAC_Address_Scraper(File):
    with open(File, 'r') as file:
        info = file.read()
    regex_pattern = re.compile(r'\w\w:?-?\w\w:?-?\w\w:?-?\w\w:?-?\w\w:?-?\w\w')
    found = re.findall(regex_pattern, info)
    MAC_Addresses = []
    MAC_Addresses_data = []
    for i in found:
        MAC_Addresses.append(i)
        i.replace(":", "%3A")
        url = "https://maclookup.app/search/result?mac=" + i
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "html.parser")
        VendorID = []
        for i in soup.find_all("p"):
            VendorID.append(i.get_text())
        MAC_Addresses_data.append(VendorID[2])
    f = open("Scraped MAC Addresses.txt", "w+")
    for i in range(len(MAC_Addresses)):
        MAC_Address = "".join(MAC_Addresses[i])
        MAC_Address_data = "".join(MAC_Addresses_data[i])
        Vendor = MAC_Address_data
        f.write(MAC_Address + " | " + Vendor + "\n")
    print("\nMAC Addresses discovered: " + str(len(MAC_Addresses)))

parser = optparse.OptionParser()
parser.add_option("-f", "--file", dest="file", help="to choose a file")
(options, arguments) = parser.parse_args()
MAC_Address_Scraper(options.file)
