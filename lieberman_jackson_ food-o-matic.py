'''
Author: Lieberman
Date: 4/4/2025
Description: This code generates a random number of menu items based on a user input
Challenges: Uses random library to get random items based on how many items the user wants, calculates the total cost of all items, uses try/except to make sure the numebr is valid,removes possiblitity for duplicate items, doesnt allow user to select too many items, hangman
'''
import random #imports the random library

mains = ['cauliflower','tilapia fillet','pork loin','salmon','potatoe','three color squash','eggplant','steak','baguette'] #list of entres
Price = [20, 25, 28, 30, 18, 20, 22, 30, 20] #list of prices
Flair = ['with balsamico', 'with garlic and olive oil', 'with minted yogurt', 'with chutney', 'salad', 'with salsa', 'over sticky rice', 'au jus', 'with basmati rice'] #list of sides

while True:#forever loop
    try:#attempt to ask the user how many items they need
        items = int(input('How many menu items do you need?'))
    except:#if it doesnt work tell the user to enter a valid number and continue the code
        print('Please enter a valid number')
        continue
    
    total = 0 #sets variable total to 0

    for i in range(items):#for the amount of items the user wanted
        main = random.choice(mains)#generates a random item from the list mains
        price = Price[mains.index(main)]#print the price of that main
        print(f'{main} {Flair[i]}, ${price}')#prints the main side and price
        total += price#add the price to the total
    print(f'Your total is ${total}')#print the total

    


