    def double_the_difference(lst):
        result = 0
        for num in lst:
            if isinstance(num, int) and num >= 0:
                if num % 2 != 0:
                    result += num ** 2
        return result
    print(double_the_difference([1, 3, 2, 0]))  
    print(double_the_difference([-1, -2, 0]))  
    print(double_the_difference([9, -2]))  
    print(double_the_difference([0]))  
    print(double_the_difference([]))   # empty list, return 0.  
    # The function should return the sum of squares of the numbers in the list that are odd. Ignore numbers that are negative or not integers.  
    # The function will return 0 if the input list is empty.  
    # For example, double_the_difference([1, 3, 2, 0]) should return 1 + 9 + 0 + 0 = 10.  
    # double_the_difference([-1, -2, 0]) should return 0, because all numbers in the list are negative or not integers.  
    # double_the_difference([9, -2]) should return 81, because 9 is the only odd number in the list.  
    # double_the_difference([0]) should return 0, because 0 is even.  
    # double_the_difference([]) should return 0, because the list is empty.  
    # The function should work correctly for these examples.  
    # The function should also work correctly for other examples that are not shown here.  
    # The function should handle edge cases correctly, such as an empty list or a list with only one element.  
    # The function should return the correct result for each example.  
    # The function should be efficient and use a reasonable amount of memory.  
    # The function should be easy to understand and maintain.  
    # The function should be well-documented with a clear description of what it does.  
    # The function should have a clear and concise name.  
    # The function should be tested thoroughly to ensure it works correctly.  
    # The function should be able to handle large input lists.  
    # The function should be able to handle input lists with many negative numbers.  
    # The function should be able to handle input lists with many even numbers.  
    # The function should be able to handle input lists