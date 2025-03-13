#!/usr/bin/env python3

# Created By: Tony G

# Date: 2025-02-19

# Shows the dimensions of a 2d circle

import math


def main():
    # asks for user input of radius and calculates circumference and area
    radius = float(input("enter radius of circle: "))
    print(" circumference = {}".format(math.pi * 2 * radius))
    print(" area = {}".format(math.pi * radius**2))


if __name__ == "__main__":
    main()
