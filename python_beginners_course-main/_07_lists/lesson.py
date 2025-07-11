my_string = input('Enter a number:')

if my_string.isdigit():
    my_integer = int(my_string)
    print(my_string)
else:
    print(f"{my_string} is not a number")