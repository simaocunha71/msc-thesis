def sum_Of_Subarray_Prod(list):
    if not list:
        return 0
    n = len(list)
    result = 0
    for i in range(n):
        for j in range(i+1, n+1):
            result += sum(list[i:j]) * (j-i)
    return result


"""
def sum_Of_Subarray_Prod(list):
    if not list:
        return 0
    n = len(list)
    result = 0
    for i in range(n):
        for j in range(i+1, n+1):
            result += sum(list[i:j]) * (j-i)
    return result
"""
# assert sum_Of_Subarray_Prod([1,2,3]) == 20
# print(sum_Of_Subarray_Prod([1,2,3]))




"""
The next great Indian Startup

Write a Python function, insertionSort, that sorts a given list of integers using insertion sort.

Test your function with the following list of integers:

assert insertionSort([8, 3, 6, 1, 7, 5, 9, 4, 2]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

To test your function, you can use Python's built-in assert statement. This statement allows you to check if a condition is true or false. If the condition is false, Python raises an AssertionError exception with the error message "assertion failed". If the condition is true, Python continues with the next line of code.

The insertion sort algorithm works by taking each element from the input list, one by one, and inserting it into the correct position in a sorted portion of the list.
"""

def insertionSort(list):
    for i in range(1, len(list)):
        currentElement = list[i]
        j = i - 1
        while j >= 0 and list[j] > currentElement:
            list[j+1] = list[j]
            j -= 1