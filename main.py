"""
 Decimal to Binary Converter

 Description: Takes the users number and converts it into binary.
 Continues doing that until the program is stopped or 'E' is entered.

 Author: Torin
 Date: March 3rd, 2026
"""

from sys import exit

def greeting():
    """
    Greets user and displays
    program overview.
    """
    print("***** DECIMAL TO BINARY CONVERTER *****\n"
          "This program converts numbers into binary.\n"
          "Insert your number at the prompt below and\n"
          "it will be converted. Enter 'E' to exit.")

greeting.called = False

def main():
    """
    Keeps asking the user for input
    until 'E' is pressed. Converts
    input into binary and displays
    the result.
    """
    if not greeting.called:
        greeting()

    while num not in ["E", "e"]:
        bin = []
        num = input("\nEnter your number: ")

        try:
            num = int(num)

        except ValueError:
            if num in ["E", "e"]:
                exit()
            else:
                exit("ERROR: Input must be a number.")

        if num == 0:
            bin.insert(0, 0)

        while num > 0:
            if num % 2 == 1:
                bin.insert(0, 1)
            else:
                bin.insert(0, 0)
            num = num // 2

        print("Your binary number: ", end='')
        print(*bin, sep='')

if __name__ == "__main__":

    main()

