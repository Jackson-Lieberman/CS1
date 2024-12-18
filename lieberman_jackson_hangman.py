import random
words = ['flamingo', 'watermelon', 'flight', 'wind', 'xylophone', "anaconda", "black", "yellow", "rainbow"]

while True:
    lives = 5
    word = random.choice(words)
    display = ["_"]*len(word)
    words.remove(word)
    
    while lives > 0 and "_" in display:
        print(' '.join(display))
        guess = input("Which letter do you want to guess?").lower()
        if guess in word:
            for index in range(len(display)):
                if guess == word[index]:
                    display[index]=guess
        else:
            print("Not in the word")
            lives -= 1
            print(f"{lives} lives remaining")
    print("The word was", word)
    if lives==0:
        print(f'You lost!')
    
    again= input("Play again?").lower()
    if again== "no":
        break
