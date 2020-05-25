from src.threenum import three_num


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


main()
