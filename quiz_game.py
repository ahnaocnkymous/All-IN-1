
print("I'm gonna be the King of the Hackers!\nI'm gonna surpass my limits right here, right now~")

print('Welcome to Fun Quizes~')
playing = input('Do you want to play? ').lower()
print(playing)

if playing != 'yes':
    quit()

print("Okay! Let's play :)")
score = 0

answer = input('What does CPU stand For? ').lower()
if answer == 'central processing unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('What does GPU stand For? ').lower()
if answer == 'graphic processing unit' or 'graphics processing unit' or 'graphical processing unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    
answer = input('What does RAM stand For? ').lower()
if answer == 'random access memory':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    
answer = input('What does PSU stand For? ').lower()
if answer == 'power supply unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    
answer = input('What does ROM stand For? ').lower()
if answer == 'read only memory':
    print('Correct!')
else:
    print('Incorrect!')

print(f"You got {score} questions correct!")
print(f"You got {((score/4)*100)} %")