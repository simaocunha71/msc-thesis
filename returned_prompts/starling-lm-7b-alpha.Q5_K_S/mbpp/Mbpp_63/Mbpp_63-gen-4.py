"""
def max_difference(t):
    # t is a list of tuples
    m = -1
    for i in range(len(t)):
        for j in range(i+1, len(t)):
            m = max(m, abs(t[i][0] - t[j][1]))
    return m

assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
"""

def max_difference(t):
    # t is a list of tuples
    m = -1
    for i in range(len(t)):
        for j in range(i+1, len(t)):
            m = max(m, abs(t[i][0] - t[j][1]))
    return m

assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7

# Python3 program to find
# maximum and minimum
# difference of pairs

# Function to find the
# maximum and minimum
# difference of pairs
def max_min_diff(t):
    # t is a list of tuples

    # Initialize max and min
    # difference
    max_diff = -1
    min_diff = float('inf')

    # Iterate through all
    # the pairs in the list
    for i in range(len(t)):
        for j in range(i+1, len(t)):

            # Calculate the difference
            diff = abs(t[i][0] - t[j][1])

            # Update max and min
            # difference
            max_diff = max(max_diff, diff)
            min_diff = min(min_diff, diff)

    # Return the max and min
    # difference
    return max_diff, min_diff

# Driver code
t = [(3, 5), (1, 7), (10, 3), (1, 2)]

max_diff, min_diff = max_min_diff(t)
print("Maximum difference is:", max