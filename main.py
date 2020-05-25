import math


def main():
    valid_input = False
    while not valid_input:
        print("Welcome to 3 like numbers!")
        try:
            value = int(input("PLease enter a positive integer: "))
        except:
            print("Invalid input. Please try again.")
            continue
        valid_input = True


main()
