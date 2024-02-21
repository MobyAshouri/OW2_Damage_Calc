from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"} 

def getAllHeroesList() -> str:
    URL = "https://overwatch.fandom.com/wiki/Heroes#Hero_roster"
    r = requests.get(URL)
    
    soup = BeautifulSoup(r.content, "html5lib")
    soup.prettify

def webScrapeWiki():
    roster = "https://overwatch.fandom.com/wiki/Heroes#Hero_roster"
    charList = ["ana","ashe","baptiste","bastion","brigitte",
                "cassidy","d.va","doomfist","echo","genji",
                "hanzo","illari","junkerqueen","junkrat","kiriko",
                "lifeweaver","lucio","mauga","mei","mercy","moira",
                "orisa","pharah","ramattra","reaper","reinhardt",
                "roadhog","sigma","sojourn","soldier", "sombra",
                "symmetra","torbjorn",""]
    URL = "https://overwatch.fandom.com/wiki/"