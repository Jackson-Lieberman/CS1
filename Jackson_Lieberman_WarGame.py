import random
suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
deck = []

for s in suits:
    for f in faces:
        deck.append(f"{f} of {s}")

hand1 = random.sample(deck, 26)

for card in hand1:
    deck.remove(card)

hand2 = random.sample(deck, 26)

name = input('''What is your name?
             ''')
print('''Hello ''' + name, " welcome to war!")
p1_score = 0
p2_score = 0

for card in hand1:
    for card in hand2:
        p1_play = input("Player 1 press enter to deal:")
        print(random.sample(hand1, 1))
        deck.remove(card)
        p2_play = input("Player 2 press enter to deal:")
        print(random.sample(hand2, 1))
        deck.remove(card)
        #if the value of p1s card is > the value of p2s card
            # p1_score += 1
        #elif the value of p2s card is > the value of p1s card
            # p2_score += 1   
        #elif value of p1==value of p2
            print('''Time for war!
                     1...
                     2...
                     3...
                     War!''')
            p1_play = input("Player 1 press enter to deal:")
            print(random.sample(hand1, 1))
            deck.remove(card)
            p2_play = input("Player 2 press enter to deal:")
            print(random.sample(hand2, 1))
            #compare again but this time for 3 points
                    
      
