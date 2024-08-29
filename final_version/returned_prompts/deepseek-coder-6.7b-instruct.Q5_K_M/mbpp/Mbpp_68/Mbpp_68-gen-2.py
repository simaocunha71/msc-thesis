def second_largest(lst):
    lst.sort()
    return lst[-2]

print(second_largest([1, 2, 3, 4, 5]))  # 4

"""
Explanation:

The function `second_largest` takes a list as input and returns the second largest number in the list.

The function first sorts the list in ascending order using the `sort` function.

The second largest number is the second last number in the sorted list, so the function returns the second last element of the list using indexing.

The index -2 refers to the second last element because Python indexing starts