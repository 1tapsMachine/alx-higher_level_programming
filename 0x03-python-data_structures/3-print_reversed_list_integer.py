#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    listLen = len(my_list)
    for i in range(listLen, 0, -1):
        print("{:d}".format(my_list[i - 1]))
