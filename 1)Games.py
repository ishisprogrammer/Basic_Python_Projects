import random
import numpy as np

def game1():
   wins = 0
   losses = 0
   try:
       n = int(input('Enter the number of matches you wanna play: '))
       if n<=0 or n>150:
           print('Pleae give a valid input\n')
           return game1()                                                       
   except:
          print('Please give a valid input\n')
          return game1()
   i = 1
   while i<=n:
           if i == 1:
                print('Enter your 1st choice:')
           elif i == 2:
                print('Enter your 2nd choice:')
           elif i == 3:
                print('Enter your 3rd choice:')
           else:
                print(f'Enter your {i}th choice')
           comp =  np.random.choice(['stone', 'paper', 'scissor'])
           user = input().lower()
           if user not in ['stone', 'paper', 'scissor']:
               print('Please give a valid input!\n')
           else:
               if (user=='stone' and comp=='paper') or (user=='paper' and comp=='scissor') or (user=='scissor' and comp=='stone'):
                    print(f"The computer chose {comp} and you chose {user}, so you lose this time\n")
                    losses+=1
               elif (user=='stone' and comp=='scissor') or (user=='paper' and comp=='stone') or (user=='scissor' and comp=='paper'):
                    print(f'The computer chose {comp} and you chose {user}, so you won this time\n')
                    wins+=1
               else:
                    print(f"The computer chose {comp} and you chose {user}, so its a draw\n")
               i+=1
   else:
        print(f'There were {wins} wins and {losses} losses\n')
        if wins>losses:
             print('Congratulations!\nYou are the winner of this series')
        elif wins<losses:
             print('Better luck next time')
        else:
             print('Its a Draw')
                
def game2():
    i=1
    comp=np.random.randint(1,150)
    while i>0:
         if i==1:
              print('Enter your 1st choice: ')
         elif i==2:
              print('Enter your 2nd choice:')
         elif i==3:
              print('Enter your 3rd choice:')
         else:
              print(f'Enter your {i}th choice')
         try:
              user=int(input())
         except:
              print('Please enter a vaid guess\n')
              continue
         if user>comp:
              print('Too high, Guess again!\n')
              i+=1
         elif user<comp:
              print('Too low, Guess again!\n')
              i+=1
         else:
              if i==1:
                 print(f'Wow!,\nYou guessed the right number in {i} turn')
                 break
              else:
                 print(f'Wow!,\nYou guessed the right number in {i} turns')
                 break
                  
def start():
    try:
       print("Enter the code of the game you wanna play:\n1.) Enter 1 to play 'Stone-Paper-Scissor'\n2.) Enter 2 to play 'Guessing the numbers'")
       game = input()
       if int(game) == 1:
           print('Great!, so lets play the game\n')
           return game1()
       elif int(game) == 2:
           print('Great!, so lets play the game\n')
           return game2()
       else:
           print('Please give a valid input!\n')
           return start()
    except:
           print('Please give a valid input\n')
           return start()

start()




   









