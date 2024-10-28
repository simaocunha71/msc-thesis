    # Initialize result
    result = []

    # Iterate through the array
    for x in arr:
        # Check if the number is between 1 and 9 inclusive
        if 1 <= x <= 9:
            # Add the number to the result
            result.append(x)

    # Sort the result
    result.sort()

    # Reverse the result
    result.reverse()

    # Initialize the mapping dictionary
    mapping = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }

    # Replace each digit in the result with its corresponding name
    for x in range(len(result)):
        result[x] = mapping.get(result[x])

    # Return the result
    return result

# Test cases
print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))  # ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
print(by_length([]))  # []
print(by_length([1, -1 , 55]))  # ['One']

# Time complexity: O(n)
# Space complexity: O(n)

# Here's a Python solution to your problem:
# The function `by_length` takes an array `arr` as input and returns an array of the corresponding names of the integers between 1 and 9, in descending order.
# The function first checks if the array is empty, and if so, it simply returns an empty array.
# Next, it iterates through each element in the array and checks if it is between 1 and 9. If it is, the number is added to the `result` array.
# After all the numbers have been collected in the `result` array, the array is sorted in ascending order using the `sort()` method, and then reversed using the `reverse()` method.
# Finally,