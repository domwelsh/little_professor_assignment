def get_integer(prompt, Min, Max):
    while True:
        try:
        #The try block lets you test a block of code for errors.
            user_input = int(input(prompt))
            if Min <= user_input <= Max:
                return user_input
        except ValueError:
        #The except block lets you handle the error.
            print("Invalid input. Please enter a valid integer between {} and {}.".format(Min, Max))
