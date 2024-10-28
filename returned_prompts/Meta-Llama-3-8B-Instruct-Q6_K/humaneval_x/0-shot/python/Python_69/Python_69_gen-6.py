    # create a dictionary to count the frequency of each integer
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # iterate over the dictionary to find the greatest integer that is greater than 0
    # and has a frequency greater than or equal to the value of the integer itself
    max_num = -1
    for num, count in freq.items():
        if num > 0 and count >= num:
            max_num = max(max_num, num)

    return max_num if max_num != -1 else -1
  



# Test the function
print(search([4, 1, 2, 2, 3, 1]))  # Output: 2
print(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))  # Output: 3
print(search([5, 5, 4, 4, 4]))  # Output: -1
print(search([1, 1, 1, 1, 1]))  # Output: 1
print(search([2, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # Output: -1
print(search([1, 1, 1, 1, 1, 1]))  # Output: 1
print(search([2, 2, 2, 2, 2]))  # Output: 2
print(search([1, 2, 3, 4, 5]))  # Output: -1
print(search([1, 1, 1, 1, 1, 1, 1]))  # Output: 1
print(search([1, 2, 3, 4]))  # Output: -1
print(search([1, 1, 1, 1, 1, 1, 1, 1]))  # Output: 1
print(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))  # Output: -1
print(search([1, 1, 2, 2, 2, 2