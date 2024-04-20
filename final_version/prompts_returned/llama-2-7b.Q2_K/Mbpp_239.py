"""
Write a function that takes in positive integers m and n and finds the number of possible sequences of length n, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m.
assert get_total_number_of_sequences(10, 4) == 4
"""
import math
def get_total_number_of_sequences(m, n):
    "This function takes in two positive integers."
    if m % n != 0:
        print('m and n must be relatively prime')
    else:
        return (n - m) // m

# test functions run in the interactive prompt
if __name__ == '__main__':
    get_total_number_of_sequences(1, 4)