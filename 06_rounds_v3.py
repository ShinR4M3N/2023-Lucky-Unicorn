"""Based on 06_round_v2
Converting v2 into a function
"""

import random


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

        # if the random number is between 6 and 36
        # user gets a donkey (subtracts $1 from balance)
        elif 6 <= number <= 36:
            token = "donkey"
            balance -= 1

        # in all other cases the token must be a horse or a zebra
        # (subtract $0.50 from the balance in either cases)
        else:
            # if the number is even, set the token to zebra
            if number %2 == 0:
                token = "zebra"
                balance -= 0.5

            #  otherwise, set the token to horse
            else:
                token = "horse"
                balance -= 0.5



        # output
        print(f"Rounds {rounds_played}. Token: {token}, Balance: ${balance:.2f}")
        if balance < 1:
            print("\nSorry but you have run out of money")
            play_again = "x"
        else:
            play_again = input(f"Your balance is ${balance:.2f}\n"
                           f"Do you want to continue? 'y' or 'x' to exit: ")
    return balance


# Main routine
starting_balance = 5
closing_balance = generate_token(starting_balance)
print(f"Thanks for playing\nYou've started with: ${starting_balance:.2f}\nAnd leaves with: ${closing_balance:.2f}")
