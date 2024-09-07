character = input("Enter a character name: ")
print("Hello " + character)
weapons = ["Bob sword", "Bob sheild", "Bob Gun"] 
            #0         #1            #2
print("Here are the possible weapons that you can choose from:  " + str(weapons))

weapon1 = weapons[0]
weapon2 = weapons[1]
weapon3 = weapons[2]
chosenWeapon = input("What weapon would you like? ")
print(chosenWeapon)
isInputInvalid = True


while isInputInvalid:
  chosenWeapon = input("What weapon would you like? ")
  if chosenWeapon == weapon1:
    print("You have chosen the Bob sword")
    isInputInvalid = False
  elif chosenWeapon == weapon2:
    print("You have chosen the Taco Sword")
    isInputInvalid = False
  elif chosenWeapon == weapon3:
    print("You have chosen the Taco Sheild")
    isInputInvalid = False
  else:
    print("Try Again")