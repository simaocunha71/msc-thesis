"""
def list_split(list_in, n):
    # Create an empty list to store the sublists
    sublists = []
    # Iterate through the list
    for i in range(len(list_in)):
        # Check if the index is divisible by n
        if i % n == 0:
            # If so, add a new sublist to the sublists list
            sublists.append([])
        # Add the current element to the sublist
        sublists[-1].append(list_in[i])
    # Return the sublists
    return sublists
"""

# Time Complexity: O(n)
# Space Complexity: O(n)

# Alternative Solution: Using the built-in Python functionality

"""
def list_split(list_in, n):
    # Create an empty list to store the sublists
    sublists = []
    # Iterate through the list
    for i in range(0, len(list_in), n):
        # Add the sublist to the sublists list
        sublists.append(list_in[i:i + n])
    # Return the sublists
    return sublists
"""

# Time Complexity: O(n)
# Space Complexity: O(n)

# Using the built-in Python functionality
def list_split(list_in, n):
    # Create an empty list to store the sublists
    sublists = [list_in[i:i + n] for i in range(0, len(list_in), n)]
    # Return the sublists
    return sublists

# Time Complexity: O(n)
# Space Complexity: O(n)

# Using the built-in Python functionality
def list_split(list_in, n):
    # Create an empty list to store the sublists
    sublists = [list_in[i:i + n] for i in range(0, len(list_in), n)]
    # Return the sublists
    return sublists

# Time Complexity: O(n)
# Space Complexity: O(n)

# Using the built-in Python functionality
def list_split(list_in, n