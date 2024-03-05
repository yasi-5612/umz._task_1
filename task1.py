user_input = input("Please enter your entry: ")

if user_input[0] in '-0123456789':
    print("The input is an integer.")
elif ',' in user_input:
    print("The input is a list.")
else:
    print("The input is a string.")