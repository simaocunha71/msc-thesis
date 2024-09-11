def frequency_lists(input_list):
    # your code goes here
    output = {}
    for item in input_list:
        for i in item:
            if i in output:
                output[i] += 1
            else:
                output[i] = 1
    return output

# Testing
assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]])=={1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}

# Additional Test Cases
print(frequency_lists([[1, 1, 1, 2, 3, 3, 3, 3, 3, 3], [1, 1, 1, 2, 3, 3, 3, 3, 3, 3], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]]))
print(frequency_lists([[1, 1, 1, 2, 3, 3, 3, 3, 3, 3], [1, 1, 1, 2, 3, 3, 3, 3, 3, 3], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]]))

# Time Complexity: O(n)
# Space Complexity: O(n)


def frequency_lists(input_list):
    # your code goes here
    output = {}
    for item in input_list:
        for i in item:
            if i in output:
                output[i] += 1
            else:
                output[i] = 1
    return output

# Testing
print(frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7,