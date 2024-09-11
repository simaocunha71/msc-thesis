def mul_even_odd(l):
    odd_list = []
    even_list = []
    for i in l:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    if len(odd_list) == 0:
        return 0
    if len(even_list) == 0:
        return 0
    else:
        return odd_list[0] * even_list[0]


# Write your tests here
def test_mul_even_odd():
    assert mul_even_odd([1,3,5,7,4,1,6,8]) == 4
    assert mul_even_odd([1,3,5,7,4,1]) == 0
    assert mul_even_odd([1,3,5,7,4]) == 0
    print("All tests passed.")


test_mul_even_odd()

"""
This function first separates the odd and even numbers in two different lists. If the length of odd list is 0, it means that there is no odd number in the given list and it returns 0. If the length of even list is 0, it means that there is no even number in the given list and it also returns 0. If both the odd and even lists are not empty, it returns the product of the first odd and first even number of the given list.
"""

# This function uses the modulo operator to check if a number is even or odd. It checks if the remainder of the division of the number by 2 is equal to 0. If it is equal to 0, it means that the number is even. If it is not equal to 0, it means that the number is odd.

# This function uses a for loop to iterate through the list. It checks each number in the list to see if it is even or odd, and then appends it to the corresponding list.

# This function uses the multiplication operator to multiply the first odd and first even number of the given list.

# This function uses the assert keyword to check if the result of the function is equal to the expected result. If the result is equal to the expected result,