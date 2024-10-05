    for i in range(2, n//2 + 1, 2):
        for j in range(i, n//2 + 1, 2):
            for k in range(j, n//2 + 1, 2):
                for m in range(k, n//2 + 1, 2):
                    if i + j + k + m == n:
                        return True
    return False
    # Time complexity: O(n^3), where n is the given number.
    # The reason is that we are using four nested loops to check all possible combinations of even numbers.
    # The outer loop runs from 2 to n/2, the second loop runs from i to n/2, the third loop runs from j to n/2,
    # and the fourth loop runs from k to n/2. This results in a total of n^3 iterations.
    # The space complexity is O(1), which means the space required does not change with the size of the input, i.e., it's constant.