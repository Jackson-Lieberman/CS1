import random

wins = [["7", "8",  "9"], ["1", "2", "3"], ["4", "5", "6"], ["1", "4", "7"], ["2", "5", "8"], ["3", "6", "9"], ["1", "5", "9"], ["3", "5", "7"]]
p1Name = input('''Welcome to Tic-Tac-Toe! 
             What's your name? ''')
start = input(f'Thank you {p1Name} would you like to play: 1 player or 2 player? Type 1 or 2: ')
while True:
    board = '''
___1___|___2___|___3___
___4___|___5___|___6___
___7___|___8___|___9___
               '''
    spaces = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    p1_used = []
    p2_used = []


    
    if start == "1":
        print('''You are Xs, the computer is Os
    Good Luck!
            ''')
        order = input('would you like to go first or second? Type 1 or 2:')
        if order == '1':
            while not any(all(move in p2_used for move in win) for win in wins) and not any(all(move in p1_used for move in win) for win in wins) and len(spaces) > 0: 
                p1_move = input(f'''Which square would you like to use?
                    {board}''')
                if p1_move in spaces:
                    board = board.replace(p1_move, "X")
                    p1_used.append(p1_move)
                    spaces.remove(p1_move)
                else:
                    print("Not a valid space!")
                    continue
                
                if any(all(move in p1_used for move in win) for win in wins):
                    print(f'''
                    {board}
                    {p1Name}, you won!''')
                    break

                p2_move = (random.choice(spaces))
                board = board.replace(p2_move, "O")
                p2_used.append(p2_used)
                spaces.remove(p2_move)
                
            if any(all(move in p2_used for move in win) for win in wins):
                print(f'''
                {board}
                {p1Name}, you lost!''')
            elif not any(all(move in p1_used for move in win) for win in wins):
                print(f'''
                {board}
                Tie!''')
        elif order == '2':
            while not any(all(move in p2_used for move in win) for win in wins) and not any(all(move in p1_used for move in win) for win in wins) and len(spaces) > 0: 
                p2_move = (random.choice(spaces))
                board = board.replace(p2_move, "O")
                p2_used.append(p2_used)
                spaces.remove(p2_move)

                p1_move = input(f'''Which square would you like to use?
                    {board}''')
                if p1_move in spaces:
                    board = board.replace(p1_move, "X")
                    p1_used.append(p1_move)
                    spaces.remove(p1_move)
                else:
                    print("Not a valid space!")
                    continue
                
                if any(all(move in p1_used for move in win) for win in wins):
                    print(f'''
                    {board}
                    {p1Name}, you won!''')
                    break
                
            if any(all(move in p2_used for move in win) for win in wins):
                print(f'''
                {board}
                {p1Name}, you lost!''')
            elif not any(all(move in p1_used for move in win) for win in wins):
                print(f'''
                {board}''')
        else:
            print('invalid input')
    elif start == "2":
        p2Name = input("player 2 what is your name?")

        print(f'''{p1Name}, you are Xs and {p2Name} is Os''')

        while not any(all(move in p1_used for move in win) for win in wins) and not any(all(move in p2_used for move in win) for win in wins) and len(spaces) > 0: 
            p1_move = input(f'''{p1Name} make your move!
                {board}''')
            if p1_move in spaces:
                board =board.replace(p1_move, "X")
                p1_used.append(p1_move)
                spaces.remove(p1_move)
            else:
                print("Not a valid space!")
                continue

            if any(all(move in p1_used for move in win) for win in wins):
                print(f'''
                {board}
                {p1Name}, you won!''')
                break

            while True:
                p2_move = input(f'''{p2Name} make your move!
                    {board}''')
                if p2_move in spaces:
                    board =board.replace(p2_move, "O")
                    p2_used.append(p2_move)
                    spaces.remove(p2_move)
                    break
                else:
                    print("Not a valid space!")
        if any(all(move in p2_used for move in win) for win in wins):
            print(f'''
            {board}
            {p2Name}, you won!''')
        elif not any(all(move in p1_used for move in win) for win in wins):
            print(f'''
            {board}
            Tie!''')
    else:
        print("invalid answer")    