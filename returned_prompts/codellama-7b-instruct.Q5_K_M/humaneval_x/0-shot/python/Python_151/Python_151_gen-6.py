
def double_the_difference(lst):
    # Check the list is not empty
    if not lst:
        return 0
    # Check the list has at least one odd number
    odd_number_found = False
    for number in lst:
        if number % 2 != 0:
            odd_number_found = True
            break
    # If the list has no odd numbers, return 0
    if not odd_number_found:
        return 0
    # Calculate the sum of squares of the odd numbers
    sum_of_squares = sum(number**2 for number in lst)
    return sum_of_squares
