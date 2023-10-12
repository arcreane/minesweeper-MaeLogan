#function to ask an input and make sure its an int
#take a string to print when asking the input
def AskInputInt(to_print):
    while True:
        num = input(to_print)
        try:
            val = int(num)
            break
        except ValueError:
            print("This is not a number. Please enter a valid number")

    return val


#function to request an input string and make sure that the response is one of the options
#take a string to print for input and a tuple of every options
def AskInputString(to_print, *options):
    while True:
        str = input(to_print + "\n")
        if str in options:
            return str
        print("You don't choose a good option! \n")


