#!/usr/bin/env python3

# Created by Tong Gong
# Created time November 2020
# This is a leap year program.


def main():
    # This is the function to get leap year.

    # Input
    userinput = input("Enter a year:")
    print("")

    # Process & output
    try:
        userinput = int(userinput)
        if userinput % 4 != 0:
            print("{} is a common year".format(userinput))
        else:
            if userinput % 100 != 0:
                print("{} is a leap year".format(userinput))
            else:
                if userinput % 400 != 0:
                    print("{} is a common year".format(userinput))
                else:
                    print("{} is a leap year".format(userinput))
    except Exception:
        print("{} is not a year!".format(userinput))


if __name__ == "__main__":
    main()
