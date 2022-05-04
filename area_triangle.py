#!/usr/bin/env python3

# Created by Peter Gemmell
# Created on May 2022
# This program calculates area of triangle using functions


def Area(height, base):

    area = height * base / 2

    print("The area of the triangle is {} cm².".format(area))


def main():

    height_input = input("Enter the height of triangle in cm : ")
    base_input = input("Enter the base of triangle in cm : ")

    try:
        height_input_int = int(height_input)
        base_given_int = int(base_input)
        Area(height_input_int, base_given_int)

    except Exception:
        print("Invalid input, please try again.")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
