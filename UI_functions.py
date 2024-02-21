import customtkinter as ctk
from PIL import Image

path = "character-images/"

def changeLeftImage(event, dropdown, imageLabel):
    selectedOption = dropdown.get()
    
    global photo
    photo=ctk.CTkImage(light_image=Image.open(f"{path}/{selectedOption}.png"), size=(200,200))
    imageLabel.configure(image=photo)