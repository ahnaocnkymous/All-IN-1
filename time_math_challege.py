print("I'm gonna be the King/Programmer!\nI'm gonna surpass my limits right here, right now~")
import time
import random

operators = ['+','-','*']
min_operand = 3
max_operand = 12

total_problems = 3
def generate_problem():
    left = random.randint(min_operand,max_operand)
    right = random.randint(min_operand,max_operand)
    operator = random.choice(operators)

    expres = str(left) + " " + operator + " " + str(right)    
    answer = eval(expres)
    return expres, answer


# expres, answer = generate_problem()
# print(expres, answer)

start_time = time.time()
wrong = 0
input("Press enter to start!")
print("---------------------------")
for i in range(total_problems):
    expres, answer = generate_problem()
    while True:
        guess = input('Problem #' + str(i + 1) + ": " + expres + " = ")
        if guess == str(answer):
            break       
        else:
            wrong += 1
            continue
end_time = time.time()
total_time = round((end_time - start_time),2)
print('-------------------------------')
print(f"You Finished! in {total_time} seconds. B'Coz Brain is braining~")