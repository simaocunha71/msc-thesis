from itertools import combinations
from collections import Counter
def find_Odd_Pair(arr,n):
    # Count the frequency of each element
    cnt = Counter(arr)

    # Initialize result
    res = 0

    # For every number in array
    for i in arr:

        # Generate all pairs of the number
        for j in combinations(arr, 2):

            # If xor value of the pair is 1
            if (i ^ j[0]) & 1:

                # Increment result
                res += 1

    # Return the result
    return res