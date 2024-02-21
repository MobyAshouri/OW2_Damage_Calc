import firebase_admin
from firebase_admin import credentials, firestore

# https://console.firebase.google.com/u/0/project/ow2-damage-calc-3884e/firestore

cred = credentials.Certificate('Secrets/ServiceAccountKey.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

def writeToDB(col: str, doc: str, data:dict):
    '''
    ## Function
    Writes data to Database. This overwrites previous data stored at the given location.
    col and doc are used to specify a location within the database.

    ## Parameters
    col (str): 
        used to specify the Database's collection. Available collections currently include:
        - Payment Info
        - configs
        - Registered Members

    doc (str):
        used to specify the Database's document within the collection

    data (dict):
        Data to write to the Database

    ## Returns
        None

    '''

    doc_ref = db.collection(col).document(doc)
    doc_ref.set(data)
    

def readFromDB(col: str, doc: str):
    '''
    ## Function
    Reads data from Database. This overwrites previous data stored at the given location.
    col and doc are used to specify a location within the database.

    ## Parameters
    col (str): 
        used to specify the Database's collection

    doc (str):
        used to specify the Database's document within the collection

    data (dict):
        Data to read from the Database

    ## Returns
        Requested Data at the specified location
        
    '''
    # get the information
    doc = db.collection(col).document(doc).get()

    # turn the information into a dictionary and return it
    returnDict = doc.to_dict()
    return returnDict

    
def appendCharacterToDB(charName: str, data:dict):
    '''
    ## Function
    Appends data to Database. This overwrites previous data stored at the given location.
    col and doc are used to specify a location within the database.

    ## Parameters
    col (str): 
        used to specify the Database's collection

    doc (str):
        used to specify the Database's document within the collection

    data (dict):
        Data to append to the Database

    ## Returns
        None
        
    '''
    # grab existing data
    try:
        information = readFromDB("characters", charName)
    except:     # if the data doesn't exist, make an empty dictionary
        information = {}
        
    # update the existing data with new incoming data
    information.update(data)
    # write that data back to the db
    writeToDB("characters", charName, information)