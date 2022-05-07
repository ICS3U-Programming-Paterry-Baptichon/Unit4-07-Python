#!/usr/bin/env python3

# created by: Paterry Baptichon 
# created on: 2022-05-06
# this program prints out integers from 1000 to 200 with five integers per line


def main():
    # this program prints out integers from 1000 to 200 with five integers
    # per line
    counter = 0

    # process of printing the integers from 1000 to 2000
    # output of  five integers per line with each integer separated by a space
    for counter in range(1000, 2001):
        if (counter + 1) % 5 == 0:
            print("{0} ".format(counter))
        else:
            print("{0} ".format(counter), end="")


if __name__ == "__main__":
    main()