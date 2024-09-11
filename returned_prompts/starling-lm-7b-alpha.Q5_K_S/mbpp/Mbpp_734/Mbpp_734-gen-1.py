def sum_Of_Subarray_Prod(lst):
    result = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
            result += reduce(lambda a, b: a*b, lst[i:j])
    return result

# assert sum_Of_Subarray_Prod([1,2,3]) == 20

"""
Explanation:
The above function takes a list as a parameter and returns the sum of the products of all possible sublists. It uses a nested loop to iterate through the list and generate all possible sublists. The reduce function is used to multiply all the elements in the sublist, and the result is added to the total sum. The function is tested with the provided assert statement, which asserts that the function correctly calculates the sum of the products of all possible sublists of the given list [1,2,3] (which is 20).
"""

"""
Explanation:
The above function takes a list as a parameter and returns the sum of the products of all possible sublists. It uses a nested loop to iterate through the list and generate all possible sublists. The reduce function is used to multiply all the elements in the sublist, and the result is added to the total sum. The function is tested with the provided assert statement, which asserts that the function correctly calculates the sum of the products of all possible sublists of the given list [1,2,3] (which is 20).
"""

"""
Explanation:
The above function takes a list as a parameter and returns the sum of the products of all possible sublists. It uses a nested loop to iterate through the list and generate all possible sublists. The reduce function is used to multiply all the elements in the sublist, and the result is added to the total sum. The function is tested with the provided assert statement, which asserts that the function correctly calculates the sum of the products of all possible sublists of the given list [1,2,3] (which is 20).
"""

"""
Explanation:
The above function takes a list as a parameter and returns the sum of the products of all possible sublists. It uses a nested loop to iterate through the list and