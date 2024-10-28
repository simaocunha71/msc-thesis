
def sum_Of_Subarray_Prod(my_list: list) -> int:
    prod = 1
    total = 0
    for i in range(len(my_list)):
        prod *= my_list[i]
        total += prod
    return total


