import json
from PIL import Image

# damage = baseDamage * headshotMultiplier * (1 + totalDamageDealtAmplification) * (1 - min(0.50, totalDamageTakenReduction + armorReduction) + damageTakenAmplification)
import customtkinter as ctk
from tkinter import ttk
import character as c

from UI_functions import changeLeftImage, changeRightImage
from webscrape import getAllHeroesList


def main():
    ctk.set_default_color_theme("theme.json")

    win = ctk.CTk()
    win.geometry("600x600")
    win.resizable(False, False)
    win.title("Overwatch 2 Damage Calculator")
    win.iconbitmap("icons/icon.ico")

    charList = getAllHeroesList()
    charList.sort()

    all_characters = []
    for character in charList:
        all_characters.append(character)
        
    dropDownFrame = ctk.CTkFrame(win)
    
    charDropDownLeft = ctk.CTkOptionMenu(dropDownFrame, values=all_characters, command=lambda event: changeLeftImage(event, charDropDownLeft, leftCharImageLabel))
    charDropDownLeft.grid(row=0, column=0, columnspan=2, sticky="e", padx=50)

    charDropDownRight = ctk.CTkOptionMenu(dropDownFrame, values=all_characters, command=lambda event: changeRightImage(event, charDropDownRight, rightCharImageLabel))
    charDropDownRight.grid(row=0, column=2, columnspan=2, sticky="w", padx=30)
    
    dropDownFrame.pack(pady=10)
    
    charFrame = ctk.CTkFrame(win)
    
    leftCharImage = ctk.CTkImage(light_image=Image.open("character-images/ana.png"),
                                 dark_image=Image.open("character-images/ana.png"),
                                 size=(200,200))
    leftCharImageLabel = ctk.CTkLabel(charFrame, image=leftCharImage, text="")
    leftCharImageLabel.grid(row=0, column=0)
    
    charImageSeparator = ttk.Separator(charFrame, orient="vertical")
    charImageSeparator.grid(row=0, column=1, sticky="ns", padx=20)

    rightCharImage = ctk.CTkImage(light_image=Image.open("character-images/ana.png"),
                                 dark_image=Image.open("character-images/ana.png"),
                                 size=(200,200))
    rightCharImageLabel = ctk.CTkLabel(charFrame, image=rightCharImage, text="")
    rightCharImageLabel.grid(row=0, column=2, pady=20)
    
    charFrame.pack()
    
    

    char = c.hero("Baptiste")
    print(char)

    win.mainloop()


main()