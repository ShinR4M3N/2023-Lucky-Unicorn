# Ask the user if they have played before
show_instruction = input("Have you played this game before? :")

# If they say yes, output 'Program Continues'
if show_instruction == "yes":
    print("Program continues")

# If they say no, output 'Display Instruction'
elif show_instruction == "no":
    print("Display instructions")

# Otherwise - show error
else:
    print("Please answer 'yes' or 'no'")
