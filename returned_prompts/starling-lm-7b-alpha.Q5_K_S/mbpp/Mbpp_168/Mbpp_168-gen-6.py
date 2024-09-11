def frequency(input_list, number):
    '''This function counts the number of occurrences of a number in a given list.'''
    count = 0
    for item in input_list:
        if item == number:
            count += 1
    return count


# Test the function
print(frequency([1,2,3], 4))  # Expected output: 0
print(frequency([1,1,2,3,4], 1))  # Expected output: 2
print(frequency([], 1))  # Expected output: 0
print(frequency([1,2,3,4,5,6], 4))  # Expected output: 0
print(frequency([], 0))  # Expected output: 0
print(frequency([1, 0, 0, 0, 0, 0, 0], 0))  # Expected output: 3
print(frequency([0], 0))  # Expected output: 1
print(frequency([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))  # Expected output: 1



# Test with negative input
print(frequency([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10], -10))  # Expected output: 1
print(frequency([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10], -1))  # Expected output: 0
print(frequency([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10], 0))  # Expected output: 0
print(frequency([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10], 1))  # Expected output: 0
print(frequency([-1, -2, -3, -4, -5, -6, -7, -8, -9, -1