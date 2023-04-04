"""LU base component - based on  00_LU_base_v1
Component added after they have been created and tested
"""
import random

# yes/no checking function...


def yes_no(question_text):
    while True:

        # Ask the user if they have played before
        answer = input("Have you played this game before?: ").lower()

        # If they say yes, output 'Program Continues'
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If they say no, output 'Display Instruction'
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # Otherwise - show error
        else:
            print("Please answer 'yes' or 'no'")


# function to display instruction
def instructions():
    print("**** How to play ****")
    print()
    print("The rule of the game will go here")
    print()


# number checking function
def num_check(question, low, high):
    error = "That was not a valid input\n " \
            "Please enter a number between {} and {}\n".format(low, high)

    # Keep asking until a valid amount (1-10) is entered
    while True:
        try:
            # ask for amount
            response = int(input(question))

            # check for number within the required range
            if low <= response <= high:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


# Function to generate random token
def generate_token(balance):

    rounds_played = 0
    play_again = ""

    # Testing loop to generate 5 tokens
    while play_again != "x":
        rounds_played += 1 # keep track of rounds
        number = random.randint(1, 100) # can only be donkey

        # adjust balance
        # if the random number is between 1 and 5
        # user gets a unicorn (add $4 to balance)
        if 1 <= number <= 5:
            token = "unicorn"
            balance += 4
            print(formatter("!", "Congratulations, you got a unicorn"))
            print()

        # if the random number is between 6 and 36
        # user gets a donkey (subtracts $1 from balance)
        elif 6 <= number <= 36:
            token = "donkey"
            balance -= 1
            print(formatter("-", "Unlucky, you got a donkey"))

        # in all other cases the token must be a horse or a zebra
        # (subtract $0.50 from the balance in either cases)
        else:
            # if the number is even, set the token to zebra
            if number %2 == 0:
                token = "zebra"
                balance -= 0.5
                print(formatter("I", "Nice try, you got a zebra"))

            #  otherwise, set the token to horse
            else:
                token = "horse"
                balance -= 0.5
                print(formatter("#", "oh no, you got a horse"))



        # output
        print(f"Rounds {rounds_played}. Token: {token}, Balance: ${balance:.2f}")
        if balance < 1:
            print("\nSorry but you have run out of money")
            play_again = "x"
        else:
            play_again = input(f"Your balance is ${balance:.2f}\n"
                           f"Do you want to continue? 'y' or 'x' to exit: ")
    return balance

# function to format text output
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


#  Main routine goes here...
print(formatter("-", "Welcome to the Lucky Unicorn Game"))
print()

played_before = yes_no("Have you played this game before?")

if played_before == "No":
    instructions()


# ask the user how much they want to play with
starting_balance = num_check("How much would you like to play with $", 1, 10)
print(f"you are playing with ${starting_balance}")



closing_balance = generate_token(starting_balance)
print(f"Thanks for playing\nYou've started with: ${starting_balance:.2f}\nAnd leaves with: ${closing_balance:.2f}")
print()
print(formatter("*", "Goodbye"))
