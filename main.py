import json
from PIL import Image

# damage = baseDamage * headshotMultiplier * (1 + totalDamageDealtAmplification) * (1 - min(0.50, totalDamageTakenReduction + armorReduction) + damageTakenAmplification)
import customtkinter as ctk
from tkinter import ttk

import character as c

def main():

    win = ctk.CTk()
    win.geometry("600x600")
    win.resizable(False, False)

    with open("characters.json", "r") as file:
        data = json.load(file)

    all_characters = []
    for character in data.keys():
        all_characters.append(character)
        
    dropDownFrame = ctk.CTkFrame(win, fg_color="gray")
    
    charDropDownLeft = ctk.CTkOptionMenu(dropDownFrame, values=all_characters)
    charDropDownLeft.grid(row=0, column=0, columnspan=2, sticky="e", padx=30)

    charDropDownRight = ctk.CTkOptionMenu(dropDownFrame, values=all_characters)
    charDropDownRight.grid(row=0, column=2, columnspan=2, sticky="w", padx=30)
    
    dropDownFrame.pack()
    
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