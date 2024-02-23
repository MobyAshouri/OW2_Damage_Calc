from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"} 

def getAllHeroesList() -> list[str]:
    """
    ## Function
        Webscrapes "https://overwatch.fandom.com/wiki/Heroes#Hero_roster" to get all hero names
        
    ## Params
        None
        
    ## Returns
        `listOfChars: list(str)` | A list of all the character names
    """
    
    URL = "https://overwatch.fandom.com/wiki/Heroes#Hero_roster"
    r = requests.get(URL)                                                   # get request for the Overwatch Heroes roster URL
    
    soup = BeautifulSoup(r.content, "html5lib")                             # create soup from the request
    table = soup.find('table', class_='listtable collapsible')              # find the table which includes all the characters
    
    if table:                                                               # if the table exists
        rows = table.find_all('tr')                                         # extract all rows from the table
        numOfChars = len(rows)-1                                            # get the number of rows (subtract 1 because it includes the table header)
        
        listOfChars = []                                                    # create an empty list of characters
        for i in range(0, numOfChars):                                      # for each character...
            cells = rows[i].find_all('td')                                  # find all the cells associated with that character in the table
            if cells:                                                       # if those cells exist
                listOfChars.append(cells[2].text.strip())                   # take the second column of the row, strip it into plain text, and append to our list
                
    return listOfChars                                                      # return our complete list of characters based on the wiki

def formatAbilityNames(inputString) -> str:
    """
    ## Function
        Formats ability names. The webScrapWiki() function doesn't
        easily grab ability names: the default keyboard is also
        concatenated to the ability name. Luckily, the keybind is always
        in all caps.
        
        This function removes all capitals letters from the end of a
        string until it meets a lowercase letter. It then returns the
        rest of the string.
        
    ## Example Usage
        ```python
        string = "BlinkLSHIFT"
        newString = formatAbilityNames(newString)
        print(newString)
        
        >> Blink
        ```
        
    ## Params
        `input_string`: (str)
            The string you want to format
        
    ## Returns
        The formatted version of your string
    """
    
    length = len(inputString)+1                                             # get the length of inputString (tiny optimization for our upcoming loop)
    newString=''                                                            # create an empty string, which will be our return
    
    stopSearchingForCaps = True                                             # create a boolean which indicates when we need to begin returning values
    for i in range(length):                                                 # run {length} number of times
        if inputString[-1*i].isupper():                                     # starting from the end of the string, if the character is capital...
            if stopSearchingForCaps:                                            # and if stopSearchForCaps is still True....
                pass                                                                # ignore this character and move on to the next one
            else:                                                               # if stopSearchForCaps is False...
                newString+=inputString[-1*i]                                        # add this character to our return string
        else:                                                               # if our character isn't capital....
            newString+=inputString[-1*i]                                        # add the character to our return string
            stopSearchingForCaps=False                                          # also, set stopSearchingForCaps to False

    return newString[::-1]


def webScrapeWiki():
    """
    ## Function
        Webscrapes the Overwatch Fandom Wiki. It essentially updates
        a database which behaves as an API for the time being. It scrapes for:
        - characters + abilities
        - damage values
        - health values
     
        It essentially updates the working database/API.
        
    ## Params
        None
        
    ## Returns
        None
    """
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