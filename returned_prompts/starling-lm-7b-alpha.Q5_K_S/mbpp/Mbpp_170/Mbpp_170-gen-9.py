def sum_range_list(lst, start, end):
    # initialize sum
    sum = 0
    # loop through the list
    for i in range(start, end + 1):
        # add the value of each element to the sum
        sum += lst[i]
    # return the sum
    return sum

# test the function
assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29
#assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 0, 10) == 64
#assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], -2, 15) == 74
#assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 0, 0) == 2
#assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 0, 1) == 3
#assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 0, 2) == 6
#assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 0, 3) == 9
#assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 0, 4) == 12
#assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 0, 5) == 15
#assert sum_range_list([2,1,5,6,8