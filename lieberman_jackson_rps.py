import random                                                               #import random library
import os                                                                   #import os library
choices= ["Scissors",'Paper','Rock']                                        #makes a list of possible choices
wins= [("Rock", "Scissors"), ("Scissors", "Paper"), ("Paper", "Rock")]      #makes list of different winning senarios
P1_score=0                                                                  #sets player 1 score to 0
P2_score=0                                                                  #sets player 2 score to 0
bot_score=0                                                                 #sets computer score to 0
name= input('Player 1 what is your name?')                                  #asks the player what their name is
print(f'''Hello {name}, welcome to rock, paper, scissors!
First to 5 wins the big trophy!''')                                         #says hello
start=str.capitalize(input('''Do you want to play against the computer or against another player?
type computer or 2 player:'''))                                             #asks if they want 2 player or computer
if start=="Computer":                                                       
    while True:                                                             #if they chose comupter then repeat this until it breaks
        user_choice= str.capitalize(input('''What is your weapon of choice: 
                                        '''))                               #asks for their chose 
        bot_choice= (random.choice(choices))                                #creates the computers choice randomly
        print(f"Bot choose {bot_choice}")                                   #prints the computers choice
        if (user_choice,bot_choice) in wins:                                #If the player wins tell them they won and add to their score
            print(f'{name} wins!')                                          
            P1_score += 1                                                   
        elif user_choice == bot_choice:                                     #if the choices are the smae tell its a tie
            print('its a tie!')                                             
        else:   
            print("You lost!")                                              #if neither work tells you lost and adds to the bots score
            bot_score += 1
        if bot_score == 5:                                                  #if the bot gets to 5 first then it will tell you lost and end the loop
            print(f'''Game over 
            You lost!''')
            break
        elif P1_score == 5:                                                 #if you get to 5 first it gives you the trophy and ends the loop
            print(f'''Game over {name} wins!!!
            Here is your trophy!
             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
              `"""""""` ''')
            break
        print("The bot's score is", bot_score)                               #shows the bots score 
        print(f"{name}'s score is {P1_score}")                               #shows the players score 
        again= input("play again?")                                          #asks if you want to play again
        if again == "no":                                                    #if they said no then stop the code
            break
elif start=="2 player":                                                      #if they said 2 player to the quesstion asking if they want 1 or 2 player
    P2_name=input("Player 2 what is your name?")                             #asks for the second players name
    while True:                                                              #in a forever loop
        P1_choice= str.capitalize(input(f'''{name} choose your weapon ({P2_name} dont look!):
                                        '''))                                #asks player 1 to chose their weapon
        os.system('cls')                                                     #clears the screen so the other player cant look
        P2_choice= str.capitalize(input(f'''Now {P2_name} choose your weapon ({name} dont look!):
                                        '''))                                #asks player 1 to chose their weapon
        os.system('cls')                                                     #clears the screen so the other player cant look           
        print(f"{name} choose {P1_choice}")                                  #prints the player 1 choice
        print(f"{P2_name} choose {P2_choice}")                               #prints the player 2 choice
        if (P1_choice, P2_choice) in wins:                                   #if player 1 won add to their score and show they won
            print(f'{name} wins!')                                           
            P1_score += 1
        elif (P2_choice, P1_choice) in wins:                                 #if player 2 won add to their score and show they won
            print(f"{P2_name} wins!")
            P2_score += 1
        else:                                                                #if neither person one then its a tie
            print('its a tie!')
        if P2_score == 5:                                                    #if player 2 has 5 points print that
            print(f'''Game over {P2_name} wins!!!
            Here is your trophy!
             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
              `"""""""` ''')
            break
        elif P1_score == 5:                                                 #if player 1 has 5 points print that
            print(f'''Game over {name} wins!!!
            Here is your trophy!
             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
              `"""""""` ''')
            break
        print(f"{name}'s score is", P1_score)                               #prints player 1s score
        print(f"{P2_name}'s score is {P2_score}")                           #prints player 1s score
        if P1_score == P2_score:                                            #prints if its tied
            print("It is currently tied")
        elif P1_score > P2_score:                                           #prints if player 1s winning
            print(f"{name} is winning!")
        else:                                                               #prints if player 2 is winning
            print(f"{P2_name} is winning!")   
else:                                                                       #if they did not say one of the options tell the user its invalid
    print("Not a valid answer") 
