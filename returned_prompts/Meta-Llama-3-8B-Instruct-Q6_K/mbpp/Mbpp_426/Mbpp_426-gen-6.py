def filter_oddnumbers(lst):
    return [num for num in lst if num % 2 != 0]
    # return [num for num in lst if num % 2 == 1]  # Alternative

# Test
print(filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # [1,3,5,7,9]
print(filter_oddnumbers([10,20,30,40,50,60,70,80,90,100])) # []


# Alternative solution:
def filter_oddnumbers(lst):
    return [num for num in lst if num % 2 == 1]  # Alternative

# Test
print(filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # [1,3,5,7,9]
print(filter_oddnumbers([10,20,30,40,50,60,70,80,90,100])) # []


# Explanation:
This is a Python function to filter out odd numbers from a given list. The function takes a list of numbers as input and returns a new list with only the odd numbers. The function uses a list comprehension to iterate over the input list and includes only the numbers that meet the condition of being odd (i.e., the remainder when divided by 2 is not 0). The function is tested with two lists: one with odd numbers and one with even numbers, to ensure that it works correctly in both cases. The function also includes an alternative solution using the same logic but with a different condition for filtering out odd numbers.