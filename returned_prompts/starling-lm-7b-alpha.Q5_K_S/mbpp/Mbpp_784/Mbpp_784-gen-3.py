def mul_even_odd(lst):
    evens = []
    odds = []
    for i in lst:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    if len(evens) == 0 or len(odds) == 0:
        return None
    else:
        return evens[0] * odds[0]





# Assert
print(mul_even_odd([1,3,5,7,4,1,6,8])) # 4
print(mul_even_odd([5,7,4,1,6,8])) # None
print(mul_even_odd([1,3,5,7,4,1])) # 6
print(mul_even_odd([1,3,5,7,4])) # None


# Test
assert mul_even_odd([1,3,5,7,4,1,6,8]) == 4
assert mul_even_odd([5,7,4,1,6,8]) == None
assert mul_even_odd([1,3,5,7,4,1]) == 6
assert mul_even_odd([1,3,5,7,4]) == None
print("All tests passed")



"""
Write a function to find the product of first even and odd number of a given list.

Explanation:
This function first initializes two lists, evens and odds. It then iterates through the given list, checking if each number is even or odd. If the number is even, it is added to the evens list, otherwise it is added to the odds list. After the lists have been populated, the function checks if either the evens or odds list is empty. If either list is empty, the function returns None, as there are no even or odd numbers to multiply. If both lists have values, the function returns the product of the first even and odd number in the lists.

In the provided tests, the function is called with a series of different lists. The expected results are provided, and the actual results are printed to ensure that the function is working correctly. Finally, a statement is printed to indicate whether all