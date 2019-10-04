#!usr/bin/env python

# Created by: Cameron Teed
# Created On: October 2019
# This can tell if your number is, equal to zero, positive or negative


def main():
    # This can tell if your number is, equal to zero, positive or negative

    # input
    number = int(input("Put in a number: "))

    # process
    if number > 0:

        # output
        print("your number is positive")

    # process
    elif number == 0:

        # output
        print("your number is equal to zero")

    # process
    else:
        number < 0

        # output
        print("your number is negative")


if __name__ == "__main__":
    main()
