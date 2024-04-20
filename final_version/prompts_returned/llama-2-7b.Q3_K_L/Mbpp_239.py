"""
Write a function that takes in positive integers m and n and finds the number of possible sequences of length n, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m.
assert get_total_number_of_sequences(10, 4) == 4
"""
# Time: O(n^2)
# Space: O(log n)
def get_total_number_of_sequences(m, n):
    for i in range(min(m,n)):
        if m-i < i:
            return 0
    return n*(n-1)/2

if __name__ == "__main__":
    import pytest