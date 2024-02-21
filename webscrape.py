from bs4 import BeautifulSoup
import requests
import re

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"} 

def getAllHeroesList() -> list[str]:
    URL = "https://overwatch.fandom.com/wiki/Heroes#Hero_roster"
    r = requests.get(URL)
    
    soup = BeautifulSoup(r.content, "html5lib")
    table = soup.find('table', class_='listtable collapsible')
    
    if table:
        rows = table.find_all('tr')
        numOfChars = len(rows)-1
        
        listOfChars = []
        for i in range(0, numOfChars):
            cells = rows[i].find_all('td')
            if cells:
                listOfChars.append(cells[2].text.strip())
                
    return listOfChars

def formatAbilityNames(input_string):
    #return re.sub(r'(\S[A-Z])', '', input_string)
    length = len(input_string)
    newString=''
    
    stopSearchingForCaps = True
    for i in range(length+1):
        if input_string[-1*i].isupper():
            if stopSearchingForCaps:
                pass
            else:
                newString+=input_string[-1*i]
        else:
            newString+=input_string[-1*i]
            stopSearchingForCaps=False

    return newString[::-1]


def webScrapeWiki():
    roster = getAllHeroesList()
    
    for hero in roster:
        URL = f"https://overwatch.fandom.com/wiki/{hero}#Abilities"
        r = requests.get(URL)
        abilityNames = []
        
        soup = BeautifulSoup(r.content, "html5lib")
        boxes = soup.find_all('div', class_='ability_details_main')
        
        for box in boxes:
            abilityNames.append(formatAbilityNames(box.find('div', class_='abilityHeader').text.strip()))
            
        print(abilityNames)
        
        #TODO
        
webScrapeWiki()