from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # Check if the list is empty
        return 0, 1  # Return 0 and 1 as per the problem statement

    total_sum = sum(numbers)  # Calculate the sum of all numbers
    total_product = 1  # Initialize product as 1
    for num in numbers:
        total_product *= num  # Calculate the product of all numbers

    return total_sum, total_product  # Return the sum and product as a tuple
    # You can test your function with the given test cases
    print(sum_product([1, 2, 3, 4]))  # Output: (10, 24) for the sum and product of the given list
    print(sum_product([]))  # Output: (0, 1) for an empty list
    # You can also add more test cases as per your requirement
    # For example:
    print(sum_product([-1, 1, 1, 0]))  # Output: (1, -1) for the sum and product of the given list
    # You can test your function with these test cases to ensure it is working correctly
    # If the function is working correctly, it should return the expected sum and product for each test case
    # If the function is not working correctly, you may need to debug it to find the issue
    # Once the function is working correctly, you can use it in your program to calculate the sum and product of any list of integers
    # For example, you can use this function in a program that calculates the sum and product of all numbers in a list
    # You can also use this function in a program that calculates the sum and product of all numbers in multiple lists
    # The possibilities are endless!