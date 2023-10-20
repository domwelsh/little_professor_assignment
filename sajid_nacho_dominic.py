import random

# global variables:
N = 10 # number of problems
T = 3 # maximum number of tries

def main():
    level = get_level()
    count_correct = 0
    for i in range(N):
        # create problem
        prompt, correct_answer = generate_prompt(level)
        # prompt for answer: the output can be True (correct answer within T tries) or False (otherwise)
        correct = get_answer(prompt, correct_answer, T)
        # update number of correct answers or provide the correct answer
        if correct:
            count_correct += 1
        else:
            print(prompt, correct_answer)
    # print score
    print("Score:", count_correct)

# input: void
# output: integer (user provided integer between 1 and 3)
def get_level():
    while True:
        try:
            level=int(input("Level: "))
            if level==1 or level==2 or level==3:
                return level
        except ValueError:
            pass

# input: integer (level)
# output: string (prompt for the user, e.g. '3 + 8 = '), integer (correct answer, e.g. 11)
def generate_prompt(level):
    num1, num2= generate_integer(level), generate_integer(level)
    correct_answer=num1+num2
    prompt=str(num1)+' + '+ str(num2)+' = '
    return prompt, correct_answer

# input: integer (level)
# output: integer (random number between 0 and 9, or between 10 and 99 or between 100 and 999)
def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    #The randint() method returns an integer number selected element from the specified range.
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level")

# input: string (prompt for user), integer (correct answer), integer (T=maximum number of tries)
# output: boolean (True is the answer is correct within T tries, and False otherwise) 
def get_answer(prompt, n, T):
    tries = 0
    while tries < T:
        guess = get_integer(prompt)
        if guess == str(n):
             return True
        else:
             print("EEE")
             tries += 1
    return False

# input: string (prompt to user), integer (minimum value for input), integer (maximum value for input)
# output: integer (user's provided integer between minimum and maximum)
# Dom - I removed (Min, Max) from params because there are no min or max values for input. The
#   code needs to accept all str's, not just numbers
def get_integer(prompt):
    return input(prompt)


# main
if __name__ == "__main__":
    main()
