#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list)
    sumi = 0
    for number in my_set:
        sumi += number
    return sumi
