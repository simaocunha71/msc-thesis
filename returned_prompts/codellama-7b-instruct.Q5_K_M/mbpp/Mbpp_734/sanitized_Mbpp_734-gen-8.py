def sum_Of_Subarray_Prod(my_list):
    result = 0
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)+1):
            result += prod(my_list[i:j])
    return result
def prod(my_list):
    result = 1
    for i in my_list:
        result *= i
    return result