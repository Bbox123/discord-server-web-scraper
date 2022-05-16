from xmlrpc.client import ServerProxy
from bs4 import BeautifulSoup
import requests
import webbrowser


class discordServer:
    def __init__(self, name, population, ID):
        self.name = name
        self.population = population
        self.ID = ID
    def serverData(self):
        serverLister(self.name, self.population, self.ID)


def serverListerFooter(desiredSize, desiredType):
    desiredType = desiredType.replace('%20', ' ')
    if (desiredSize == 1):
        print("These are all the small sized " + desiredType + " discord servers")
    if (desiredSize == 2):
         print("These are all the medium sized " + desiredType + " discord servers")
    if (desiredSize == 3):
        print("These are all the large sized " + desiredType + " discord servers")
    if (desiredSize == 4):
        print("These are all the massive " + desiredType + " discord servers")
    if (desiredSize == 5):
        print("These are all the " + desiredType + " discord servers")

def serverLister(Name, Population, serverID):
    Population = str(Population)
    print('Server name: ' + Name)
    print('Population: ' + Population + ' members')
    print('https://discordservers.com' + serverID)
    print()

def sizeChoice(choice):
    desiredSizeInt = 0
    if choice == "1":
        desiredSizeInt = 50
    if choice == "2":
        desiredSizeInt = 500
    if choice == "3":
        desiredSizeInt = 1000
    if choice == "4":
        desiredSizeInt = 2000
    if choice == "5":
        desiredSizeInt = 0
    return desiredSizeInt

def sizeChoiceList():   
    print()
    print ("Server size?")
    print ("[1] small (~50 members)")
    print("[2] medium (~500 members)")
    print("[3] large (~1000 members)")
    print("[4] massive (2000+ members)")
    print("[5] any")
    desiredSize = input("Server size: ")

    while desiredSize != '1' and desiredSize != '2' and desiredSize != '3' and desiredSize != '4' and desiredSize != '5':
        
        print("INVALID INPUT, TRY AGAIN")
        print ("Server size?")
        print ("[1] small (~50 members)")
        print("[2] medium (~500 members)")
        print("[3] large (~1000 members)")
        print("[4] massive (2000+ members)")
        print("[5] any")
        desiredSize = input("Server size (1-5): ")
    
    desiredSiInt = sizeChoice(desiredSize)
    print()
    return desiredSiInt


print("What type of discord server do you want to join?")
print("Example input: 'finance', 'art', 'monkey', 'risk of rain'")
tag = input("Server type: ")
tag = tag.lower()
#handles spaces
tag = tag.replace(' ', '%20')

desiredSizeInt = sizeChoiceList()

url = "https://discordservers.com/search/" + tag
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
html_text = requests.get(url, headers=headers).text
soup = BeautifulSoup(html_text, 'lxml')
servers = soup.find_all('section', class_ = 'Server_server__FXGWn h-server border border-dark w-full flex relative m-1 rounded-lg items-center text-left bg-dark cursor-pointer overflow-hidden shadow-md')

if not servers:
    #runs another search with the same tag but capitalized
    url = "https://discordservers.com/search/" + tag.capitalize()
    html_text = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html_text, 'lxml')
    servers = soup.find_all('section', class_ = 'Server_server__FXGWn h-server border border-dark w-full flex relative m-1 rounded-lg items-center text-left bg-dark cursor-pointer overflow-hidden shadow-md')
    if not servers:
        print("no discord servers found")

serverList = []
# this is so dumb, why can't I just track it in the for loop


for server in servers:
    serverNameRaw = server.find('a', class_ = 'mt-4 mb-2 text-2xl truncate max-w-11/12 text-gray-300')
    serverName = server.find('a', class_ = 'mt-4 mb-2 text-2xl truncate max-w-11/12 text-gray-300').text
    serverPopulation = server.find('div', class_ = 'text-gray-300 w-full my-1 mx-0 font-bold').text
    serverPop = serverPopulation.replace(",", "")
    serverID = serverNameRaw.get('href')
    serverPop = int(serverPop)
    # I could not think of any math on the spot to do this in one line sorry
    if (desiredSizeInt == 50 and serverPop > 0 and serverPop <= 100):
        serverList.append(discordServer(serverName, serverPop, serverID))  
    if (desiredSizeInt == 500 and serverPop > 100 and serverPop <= 1000):
        serverList.append(discordServer(serverName, serverPop, serverID))  
    if (desiredSizeInt == 1000 and serverPop > 1000 and serverPop <= 2000):
        serverList.append(discordServer(serverName, serverPop, serverID))  
    if (desiredSizeInt == 2000 and serverPop > 2000):
        serverList.append(discordServer(serverName, serverPop, serverID))  
    if (desiredSizeInt == 0):
        serverList.append(discordServer(serverName, serverPop, serverID))  
    

    
    #print('Server name: ' + serverName)
    #print('Population: ' + serverPopulation + ' members')
serverListerFooter(desiredSizeInt, tag)
for h in range(0, len(serverList)):
    serverList[h].serverData()

#url2 = "https://discordservers.com" + serverNameRaw.get('href')
#webbrowser.open_new_tab(url2)

#print(html_text)
