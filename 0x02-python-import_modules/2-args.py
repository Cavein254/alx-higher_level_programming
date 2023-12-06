#!/usr/bin/python3
import sys
counter = 1
num_of_args = len(sys.argv) - 1
if (num_of_args < 1):
    print("0 arguments")
elif (num_of_args == 1):
    print("1 argument")
    print("1: {}".format(sys.argv[1]))
else:
    print("{} arguments".format(num_of_args))
    while ((num_of_args > 2) and (counter != num_of_args + 1)):
        print("{}: {}".format(counter, sys.argv[counter]))
        counter = counter + 1
