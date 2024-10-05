# Rounding a number to the upper int(Ceiling) can be achieved by adding 0.5 to the number
# then converting it to int, because when a number is added with 0.5, it rounds up to the next integer
# For example: 2.5 + 0.5 = 3
#              -2.4 + 0.5 = -2.0 (as -2.4 + 0.5 = -2.9, and when rounded up, it becomes -2.0)

    # Create an empty list to store the rounded up numbers
    rounded_up_lst = []

    # Iterate through each element in the given list
    for element in lst:
        # Round each element to the upper int and append it to the new list
        rounded_up_lst.append(int(element + 0.5))

    # Create a variable to store the sum of squares
    sum_of_squares = 0

    # Iterate through each element in the rounded up list
    for element in rounded_up_lst:
        # Square each element and add the result to the sum of squares
        sum_of_squares += element ** 2

    # Return the sum of squares rounded up to the nearest integer
    return int(sum_of_squares)

# Example usage:
# lst = [1,2,3]
# print(sum_squares(lst))  # Output: 14

# lst = [1,4,9]
# print(sum_squares(lst))  # Output: 98

# lst = [1,3,5,7]
# print(sum_squares(lst))  # Output: 84

# lst = [1.4,4.2,0]
# print(sum_squares(lst))  # Output: 29

# lst = [-2.4,1,1]
# print(sum_squares(lst))  # Output: 6














```