"""
Write a python function to count the number of positive numbers in a list.
assert pos_count([1,-2,3,-4]) == 2
"""
from typing import List

def is_positive(num:int) ->bool :
    return num > 0 

def get_length(my_list):
    return len(my_list)

def is_empty(my_list):
    if get_length(my_list) == 0 :
        return True
    else :
        return False

if __name__ == "__main__":
    my_list = [1,-2,3,-4]
    #check the length of the list and check whether it contains negative values or not.
    if get_length(my_list) == 0:
        print("The input is empty.")
    else :
        for i in range(0,get_length(my_list)):
            if is_positive(my_list[i]) == False:
                print("The list contains negative values so the total number of positive numbers will be 0")
                break
        else:
            #check whether it's empty or not
            if is_empty(my_list):
                print("The input is empty.")
                break
    