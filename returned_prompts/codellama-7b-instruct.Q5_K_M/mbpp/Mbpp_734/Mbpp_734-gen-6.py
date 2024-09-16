"""
def sum_Of_Subarray_Prod(my_list):
    return sum([reduce(lambda x,y: x*y, my_list[i:j+1]) for i in range(len(my_list)) for j in range(i,len(my_list))])
"""
