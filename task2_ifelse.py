#write a rust program that takes user input and determines its type based on input 


# Get user input
user_input = input("Enter something: ")

# Check if user input is a boolean value
if user_input.lower() == 'true' or user_input.lower() == 'false':
    print("You entered a boolean value:", type(user_input))
else:
    if user_input == '_':
        print("You entered an underscore:", type(user_input))
    elif user_input.isdigit():
        number = int(user_input)
        if number < 0:
            print("You entered a negative integer number:", type(number))
        elif number > 0:
            print("You entered a positive integer number:", type(number))
        else:
            print("You entered zero:", type(number))
    elif user_input.replace('.', '', 1).isdigit():
        number = float(user_input)
        print("You entered a float number:", type(number))
    elif user_input.strip() == '':
        print("You entered an empty string:", type(user_input))
    elif user_input.isalpha():
        print("You entered a string:", type(user_input))
    else:
        print("Others")
