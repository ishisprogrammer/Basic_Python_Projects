import numpy as np

def game1():
    wins = 0
    losses = 0
    while True:
        try:
            n = int(input('Enter the number of matches you want to play: '))
            if n <= 0 or n > 150:
                print('Please give a valid input\n')
                continue                        
            else:
                break                      
        except (ValueError, TypeError):
            print('Please give a valid input\n')
            continue
    i = 1
    while i<=n:
        suffix = ['st' if i == 1 else 'nd' if i == 2 else 'rd' if i == 3 else 'th']
        print(f'Enter your {i}{suffix[0]} choice')
        comp = np.random.choice(['stone', 'paper', 'scissor'])
        user = input().lower()
        if user not in ['stone', 'paper', 'scissor']:
            print('Please give a valid input!\n')
            continue
        else:
            if (user == 'stone' and comp == 'paper') or (user == 'paper' and comp == 'scissor') or (user == 'scissor' and comp == 'stone'):
                print(f"The computer chose {comp} and you chose {user}, so you lose this time\n")
                losses += 1
            elif (user == 'stone' and comp == 'scissor') or (user == 'paper' and comp == 'stone') or (user == 'scissor' and comp == 'paper'):
                print(f'The computer chose {comp} and you chose {user}, so you won this time\n')
                wins += 1
            else:
                print(f"The computer chose {comp} and you chose {user}, so it's a draw\n")
            i += 1
    else:
        print(f'There were {wins} wins and {losses} losses\n')
        if wins > losses:
            print('Congratulations!\nYou are the winner of this series')
        elif wins < losses:
            print('Better luck next time')
        else:
            print("It's a draw")
                
def game2():
    i = 1
    comp = np.random.randint(1, 150)
    print('Please enter a number between 1 and 150.')
    while True:
        suffix = ['st' if i == 1 else 'nd' if i == 2 else 'rd' if i == 3 else 'th']
        print(f'Enter your {i}{suffix[0]} choice')
        try:
            user = int(input())
        except (ValueError, TypeError):
            print('Please enter a valid guess\n')
            continue
        if user > comp:
            print('Too high, guess again!\n')
            i += 1
        elif user < comp:
            print('Too low, guess again!\n')
            i += 1
        else:
            turn=['turn' if i==1 else 'turns']
            print(f'Wow!\nYou guessed the right number in {i} {turn[0]}')
            break
                  
def start():
    while True:
        try:
            print("Enter the code of the game you want to play:\n1.) Enter 1 to play 'Stone-Paper-scissor'\n2.) Enter 2 to play 'Guess the numbers'")
            game = int(input())
            if game == 1:
                print("Great! Let's play the game\n")
                return game1()
            elif game == 2:
                print("Great! Let's play the game\n")
                return game2()
            else:
                print('Please give a valid input!\n')
                continue
        except (ValueError, TypeError):
            print('Please give a valid input\n')
            continue

start()

