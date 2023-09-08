#!/usr/bin/python3
def print_list_integer(my_list=[]):
    len = len(my_list)
    for i in range(len):
        print("{:d}".format(my_list[i]))
