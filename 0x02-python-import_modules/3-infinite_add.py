#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    counter = 1
    sum = 0
    num_of_args = len(sys.argv) - 1
    if (num_of_args < 1):
        sum = 0
    elif (num_of_args == 1):
        sum = sys.argv[1]
    else:
        while ((num_of_args >= 2) and (counter != num_of_args + 1)):
            sum += int(sys.argv[counter])
            counter = counter + 1
    print("{}".format(sum))
