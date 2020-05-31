from src.threenum import three_num
from src.threenum import is_three_like
from src.threenum import digit_three_like


def main():
    value = None
    valid_input = False
    while not valid_input:
        print("Welcome to 3 like numbers!")
        try:
            value = int(input("PLease enter a positive integer: "))
        except ValueError:
            print("Invalid input. Please try again.")
            continue
        valid_input = True

    output = three_num(value)
    print("There", ("is" if output == 1 else "are"), output, "total substrings within", value,
          "that are divisible by 3.")

    print(value, ("is" if is_three_like(value) else "is not"), "three-like.")

    digit_value = int(input("Please enter a digit you would like to try: "))

    print("There are", digit_three_like(digit_value), str(digit_value) + "-digit numbers that are three-like.")


main()
