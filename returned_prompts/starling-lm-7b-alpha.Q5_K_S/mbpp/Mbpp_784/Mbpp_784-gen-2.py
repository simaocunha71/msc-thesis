def mul_even_odd(lst):
    even_list = []
    odd_list = []
    for i in lst:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return even_list[0] * odd_list[0]


print(mul_even_odd([1,3,5,7,4,1,6,8]))














"""
In the given function, we first create two lists to store the even and odd numbers. We then iterate through the input list and append the even numbers to the even_list and the odd numbers to the odd_list. Finally, we return the product of the first even and the first odd number of these two lists.
"""
"""
The time complexity of this function is O(n), where n is the length of the input list. We iterate through the list once, which takes linear time. The space complexity is also O(n), as we create two new lists to store the even and odd numbers.
"""
"""
This function assumes that the input list contains at least one even and one odd number. If the input list does not satisfy this assumption, the function will raise an error. To prevent this, you can add a check at the beginning of the function to ensure that the input list has at least one even and one odd number.
"""
"""
To improve the function, you can consider the following optimizations:
1. Use a single list to store both even and odd numbers, and separate them later. This reduces the space complexity from O(n) to O(1).
2. Use a single variable to keep track of the product of the first even and odd numbers encountered, instead of using two separate variables. This reduces the space complexity from O(1) to O(1).
3. If the input list has an odd number of elements, you can calculate the product of all the elements instead of only the first even and odd numbers. This provides a more general solution that can handle input lists of any length.
"""
"""
To test the function, you can use the assert statement to check if the function returns the expected result for a given test case. In the provided code, the assert statement is used to check