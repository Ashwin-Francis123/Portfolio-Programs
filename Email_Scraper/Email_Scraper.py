import re
import optparse

def Email_Scraper(File):
    with open(File, 'r') as file:
        info = file.read()
    Email_regex = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9_.+-]+")
    Extracted_Emails = Email_regex.findall(info)
    f = open("Scraped_Emails.txt", "w+")
    for i in Extracted_Emails:
        f.write(i+"\n")
    print(f"[+] {str(len(Extracted_Emails))} emails discovered")
    print(f"[+] Emails have been saved to Scraped_Emails.txt")
    
parser = optparse.OptionParser()
parser.add_option("-f", "--file", dest="file", help="to choose a file")
(options, arguments) = parser.parse_args()
Email_Scraper(options.file)
