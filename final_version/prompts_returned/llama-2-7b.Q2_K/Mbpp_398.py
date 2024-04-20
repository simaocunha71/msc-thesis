"""
Write a function to compute the sum of digits of each number of a given list.
assert sum_of_digits([10,2,56])==14
"""

def sum_of_digits(nums):
    #write your code here 
    if type(nums) is list:
        nums_list = [str(i)+' ' for i in range(len(nums))]
    else:
        nums_list = str(nums)+' '
    new_string = ''    
    for char in nums_list:
        if int(char) > 1 and (not new_string):
            sum_of_digits(str(int(char))) + ' '
            else:
                new_string += str(int(char))+' '
    return new_string[:-2]
