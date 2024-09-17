```
def is_product_even(lst):
    product = 1
    for num in lst:
        product *= num
    return product % 2 == 0
``` 

This function takes a list of numbers as input, calculates the product of all numbers in the list, and returns True if the product is even (i.e., the remainder when divided by 2 is 0), and False otherwise. The unit test `assert is_product_even([1,2,3])` ensures that the function works correctly. 

The time complexity of this function is O(n), where n is the number of elements in the list, because it needs to iterate over each element in the list to calculate the product. The space complexity is O(1), because it uses a constant amount of space to store the product and the result. 

Note: The function assumes that the input list is not empty. If the input list is empty, the function will raise a ZeroDivisionError when trying to calculate the product. If you want to handle the case of an empty list, you can add a simple check at the beginning of the function: `if not lst: return True`. This is because the product of an empty list is considered to be 1, which is an even number. 

Also, the function will return True for an empty list, because the product of an empty list is considered to be 1, which is an even number. If you want to return False for an empty list, you can modify the function to return False when the input list is empty. 

It's worth noting that the function does not raise an exception if the product is 0. If you want to raise an exception in this case, you can modify the function to raise a ZeroDivisionError when the product is 0. 

Finally, the function does not handle the case where the input list contains non-numeric values. If you want to handle this case, you can add a check to ensure that all elements in the list are numeric. If a non-numeric value is found, you can raise a ValueError or return an error message. 