"""Components added after they have been created and tested
"""

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


#  Main routine goes here...

played_before = yes_no("Have you played this game before?")

if played_before == "No":
    instructions()


# ask the user how much they want to play with
user_balance = num_check("How much would you like to play with $", 1, 10)
print(f"you are playing with ${user_balance}")

