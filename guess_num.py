print("I'm gonna be the King of Hackers/Programmers\nI'm gonna surpass my limits right here, right now~")
import random
print('U r Entering in Guessing the Number game input a number u go upto guessing...')
whole_range_of_num = input('Type a Number: ')

if whole_range_of_num.isdigit():
    whole_range_of_num = int(whole_range_of_num)
    
    if whole_range_of_num <=0:
        print('please type a number larger than 0 next time.')
        quit()
else:
    print('please type a number next time')
    quit()  
random_num = (random.randint(0,whole_range_of_num))
# print(random_num)

guesses = 0 
while True:
    guesses += 1
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('please type a number next time')
        continue 

    if user_guess == random_num:
        print("You got it!",end='')
        break
    elif user_guess > random_num:
        print('Try lesser number next time.')
    elif user_guess < random_num:
        print('Try greater number next time.')
    else:
        print('You got it wrong! Try again...')
    
print(f" in {guesses} guesses~")