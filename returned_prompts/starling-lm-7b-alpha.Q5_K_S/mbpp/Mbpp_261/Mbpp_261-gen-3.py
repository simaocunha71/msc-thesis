def division_elements(tup1, tup2):
    """
    This function takes in two tuples and performs mathematical division operation element-wise across the given tuples.
    """
    res = []
    for i in range(len(tup1)):
        res.append(tup1[i]/tup2[i])
    return tuple(res)

# assert division_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)

# Explanation:
# The function "division_elements" takes two tuples as input and initializes an empty list called "res" to store the results of the division operation. It then uses a for loop to iterate through the indices of the tuples. Within the loop, it performs the division of the corresponding elements of the tuples and appends the result to the "res" list. Finally, the function returns the "res" list as a tuple.
# The provided assert statement tests the function by passing in the tuples (10, 4, 6, 9) and (5, 2, 3, 3) as arguments to the function. It then compares the result of the function with the expected output of (2, 2, 2, 3) and asserts that they are equal.

# Time Complexity: O(n), where n is the length of the tuples. This is because the function iterates through the tuples only once, performing the division operation for each pair of corresponding elements.

# Space Complexity: O(n), where n is the length of the tuples. This is because the function creates a new list called "res" to store the results of the division operation, and the length of the list is equal to the length of the tuples.

# Big O Notation Explanation:
# Time Complexity: O(n) - The function iterates through the tuples only once, performing the division operation for each pair of corresponding elements. This means that the time complexity of the function is proportional to the length of the tuples.

# Space Complexity: O(n) - The function creates a new list called "res" to store the results of the division operation.