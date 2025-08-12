print("I'm gonna be the King of the Hackers/Programmer!\nI'm gonna surpass my limits right here, right now~")
import random


user_wins = 0
computer_wins = 0

option1 = ['rock','paper','scissors']
while True:
    user_input = input('Pick a Move: Rock,Paper,Scissors\nor Q to quit:- ').lower()
    if user_input == 'q':
        break


    if user_input not in option1:
        continue

    random_num = random.randint(0,2)
    # rock:0, paper:1, scissors:2

    computer_pick = option1[random_num] 
    print('Computer Picked',computer_pick , '.')

    if user_input == 'rock' and computer_pick == 'scissors':
        print('Yon won!')
        user_wins += 1

    elif user_input == 'paper' and computer_pick == 'rock' :
        print('Yon won!')
        user_wins += 1

    elif user_input == 'scissors' and computer_pick == 'paper':
        print('Yon won!')
        user_wins += 1
    else:
        computer_wins += 1
        print('You lose~')

print(f"You won! {user_wins} times.")
print(f"Computer won! {computer_wins} times.")
print('Sayonara!')