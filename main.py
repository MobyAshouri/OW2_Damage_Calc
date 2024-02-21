import json

# damage = baseDamage * headshotMultiplier * (1 + totalDamageDealtAmplification) * (1 - min(0.50, totalDamageTakenReduction + armorReduction) + damageTakenAmplification)
import customtkinter as ctk

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
    

    char = c.hero("Baptiste")
    print(char)

    win.mainloop()


main()