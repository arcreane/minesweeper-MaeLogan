
def AskInputInt(to_print):
    """
       Prompt the user for input and validate it as an integer.

       This function displays the provided message and continuously prompts the user
       for input until a valid integer is provided. If the user enters a non-integer value,
       an error message is displayed, and the user is prompted again.

       Parameters:
       - to_print (str): The message to display to the user when requesting input.

       Returns:
       int: The validated integer input provided by the user.

       Example Usage:
       - width = AskInputInt("Enter field width: ")  # Example usage to get an integer input.
       """
    while True:
        num = input(to_print)
        try:
            val = int(num)
            break
        except ValueError:
            print("This is not a number. Please enter a valid number")

    return val


def AskInputString(to_print, *options):
    """
        Prompt the user for input and validate it against a set of specified options.

        This function displays the provided message and continuously prompts the user
        for input until a valid option from the provided set of options is entered. If the
        user enters an invalid option, an error message is displayed, and the user is prompted again.

        Parameters:
        - to_print (str): The message to display to the user when requesting input.
        - *options (str): Variable number of strings representing the valid options.

        Returns:
        str: The validated string input provided by the user, matching one of the specified options.

        Example Usage:
        - choice = AskInputString("Choose an option:", "Yes", "No", "Quit")
          # Example usage to get a string input from a set of options ("Yes", "No", "Quit").
        """
    while True:
        str = input(to_print + "\n")
        if str in options:
            return str
        print("You don't choose a good option! \n")


