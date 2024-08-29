def sum_range_list(lst, start, end):
    return sum(lst[start:end+1])

print(sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10)) # 29

"""
The function sum_range_list takes a list and two indices as input. It uses slicing to get the sublist from the start index to the end index (inclusive). It then computes the sum of the elements in the sublist using the sum() function and returns the result.
"""


"""
