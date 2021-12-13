# Modules
import subprocess
import random
import re
import optparse
from time import sleep
 
 
# Function to create random MAC Address
def random_mac_address_creator():
    First_Octet = ""
    Second_Octet = ""
    Third_Octet = ""
    Fourth_Octet = ""
    Fifth_Octet = ""
    Sixth_Octet = ""
 
    Letters = ["A", "B", "C", "D", "E", "F"]
    Even_Numbers = [2, 4, 6, 8]
 
    Number = str(random.choice(Even_Numbers))
    First_Octet += Number
    First_Octet += Number
 
    Number = str(random.randint(1, 9))
    Letter = random.choice(Letters)
    Second_Octet += Letter
    Second_Octet += Number
 
    Number = str(random.randint(1, 9))
    Letter = random.choice(Letters)
    Third_Octet += Number
    Third_Octet += Letter
 
    Number = str(random.randint(1, 9))
    Letter = random.choice(Letters)
    Fourth_Octet += Letter
    Fourth_Octet += Number
 
    Number = str(random.randint(1, 9))
    Letter = random.choice(Letters)
    Fifth_Octet += Number
    Fifth_Octet += Letter
 
    Number = str(random.randint(1, 9))
    Letter = random.choice(Letters)
    Sixth_Octet += Letter
    Sixth_Octet += Number
 
    MAC_Address = f"{First_Octet}:{Second_Octet}:{Third_Octet}:{Fourth_Octet}:{Fifth_Octet}:{Sixth_Octet}"
    return MAC_Address
MAC_Address = random_mac_address_creator()
 
 
# Function to check if MAC address is valid
def isValidMACAddress(str):
    #Regex rules for validator
    regex = ("^([0-9A-Fa-f]{2}[:-])" +
            "{5}([0-9A-Fa-f]{2})|" +
            "([0-9a-fA-F]{4}\\." +
            "[0-9a-fA-F]{4}\\." +
            "[0-9a-fA-F]{4})$")
 
    p = re.compile(regex)
 
    if (str == None):
        return False
 
    if(re.search(p, str)):
        return True
    else:
        return False

if isValidMACAddress(MAC_Address):
   valid_MAC_Address = MAC_Address
  
# Function to execute commands into terminal
def mac_change_commands(interface):
    print(f"[+] Changing MAC Address for {interface}\n")
    subprocess.call(f"sudo ifconfig {interface} down", shell=True)
    subprocess.call(f"sudo ifconfig {interface} hw ether {valid_MAC_Address}", shell=True)
    subprocess.call(f"sudo ifconfig {interface} up", shell=True)
    # This bit below prints all the commands used so users know what's going on
    print(f"sudo ifconfig {interface} down")
    print(f"sudo ifconfig {interface} hw ether {MAC_Address}")
    print(f"sudo ifconfig {interface} up\n")
    print(f"[+] New MAC Address for {interface}: {MAC_Address}")
parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="to assign an interface")
(options, arguments) = parser.parse_args()
mac_change_commands(options.interface)
