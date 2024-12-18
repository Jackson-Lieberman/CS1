import random                                                                                                 #imports random library

name = input ("what is your name? ")                                                                          #asks the user their name
print(f"Good luck {name}!")                                                                                   #tells the user good luck
words = ['flamingo', 'watermelon', 'flight', 'wind', 'xylophone', "anaconda", "black", "yellow", "rainbow"]   #makes a list of words
Games = 0                                                                                                     #sets wins to 0
Wins = 0                                                                                                      #sets games to 0
 
while True:                                                                                                   #repeat forever
    word = random.choice(words)                                                                               #chose a random word from the list
    letters = list(word)                                                                                      #makes a list from the letters in the word
    random.shuffle(letters)                                                                                   #shuffles the letters 
    display = ''.join(letters)                                                                                #combines the letters into a string
    turns = 5                                                                                                 #sets turns to 5
    print("You have 5 turns to guess the word")                                                               #tell the user they have 5 turns

    while turns > 0:                                                                                          #repeat while you have more turns than 0
        guess=input("Unscramble " + display + " ")                                                            #tells the user to unscramble the scrambled word

        if guess == word:                                                                                     #if the guess is correct
            print("You got it!")                                                                              #tell the user they were correct
            Wins +=1                                                                                          #add to their wins
            break                                                                                             #end the loop
        
        while True:                                                                                           #repeat forever
            scramble = str.lower(input(f"You have {turns} turns left. Would you like to rescramble again? yes/no: "))                       #ask the user if they want to play again
            
            if scramble == "no":                                                                              #if they dont want to play again
                break                                                                                         #end the code
            elif scramble == "yes":                                                                           #if they said yes
                letters = list(word)                                                                          #make a list from the random word
                random.shuffle(letters)                                                                       #shuffles the letters 
                display = ''.join(letters)                                                                    #combines the letters into a string
                break                                                                                         #end the loop
            else:                                                                                             #if their yes or no was said
                print("invalid input!")                                                                       #tell them it was invalid
        turns -= 1                                                                                            #subtract one from their turns
    print(word)                                                                                               #show the word
    Games += 1                                                                                                #add one to the users games

    play = str.lower(input(f"You have won {Wins} out of {Games} games. Would you like to play again? "))      #tells them how many wins they have out how ever many games and ask if they want to play again

    if play == "no":                                                                                          #If they said no
        break                                                                                                 #end the loop
