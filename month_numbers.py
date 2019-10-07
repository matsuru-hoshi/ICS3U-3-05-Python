#!/usr/bin/env python3

# Created by: Matsuru Hoshi
# Created on: Oct 2019
# This is program tells you the month based on the number inputed


def main():
    # funciton prints month based on number inputed

    # Welcome statement
    print("Hi, input a number and I will give you the corresponding month.")
    input("Press Enter to continue.")

    # input
    number = float(input("What is your number: "))

    # process
    if number == 1:
        print("January")
    elif number == 2:
        print("February")
    elif number == 3:
        print("March")
    elif number == 4:
        print("April")
    elif number == 5:
        print("May")
    elif number == 6:
        print("June")
    elif number == 7:
        print("July")
    elif number == 8:
        print("August")
    elif number == 9:
        print("September")
    elif number == 10:
        print("October")
    elif number == 11:
        print("November")
    elif number == 12:
        print("Decemeber")
    else:
        print("Invalid input")


if __name__ == "__main__":
    main()
