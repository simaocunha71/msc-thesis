
def issort_list(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

print(issort_list([1,2,4,6,8,10,12,14,16,17]))


"""
Given a list of integers, write a function that returns the largest product of any three numbers in the list.

For example, if the list is [-10, -10, 1, 3, 2] the function should return 300, which is the product of -10, -10 and 3.

