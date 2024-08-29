def pair_xor_Sum(arr,n):
    sum = 0
    for i in range(0, n):
        for j in range(i+1, n):
            sum += arr[i] ^ arr[j]
    return sum

print(pair_xor_Sum([5,9,7,6],4)) # Output: 47

Explanation:
The function pair_xor_Sum takes a list and its size as input and initializes a variable sum to 0. 
The function then uses two nested for loops to iterate over all possible pairs of numbers in the list. 
For each pair, it computes the bitwise XOR (^) of the two numbers and adds the result to the sum. 
Finally, it returns the sum.
"""

# Task 2

"""
