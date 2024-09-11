def pair_xor_Sum(arr,n):
    result = 0
    for i in range(n):
        for j in range(i+1,n):
            result += arr[i]^arr[j]
    return result

print(pair_xor_Sum([5,9,7,6],4))






"""
def pair_xor_Sum(arr,n):
    result = 0
    for i in range(n):
        for j in range(i+1,n):
            result += arr[i]^arr[j]
    return result

# Driver program
arr = [5, 9, 7, 6]
n = len(arr)
print(pair_xor_Sum(arr,n))"""

"""
In the above code, we define a function named pair_xor_Sum which takes two parameters: arr and n. Here, arr is the list of numbers and n is the length of the list. Inside the function, we initialize a variable result to 0 which will hold the sum of the XOR of all pairs of numbers.

We use two nested for loops to iterate through all the possible pairs of numbers in the given list. The outer loop iterates from 0 to n-1 and the inner loop iterates from i+1 to n-1. This is done to avoid repetition of pairs. For each pair of numbers, we calculate the XOR using the bitwise XOR operator (^) and add the result to the variable result.

Finally, we return the value of result which is the sum of the XOR of all pairs of numbers in the given list. In the driver program, we define a list of numbers arr and calculate its length n. Then we call the pair_xor_Sum function with arr and n as arguments and print the result.
"""


"""
The time complexity of the above code is O(n^2) because we are using two nested for loops. The space complexity is O(1) because we are not using any extra space that grows with the size of the input.
"""


"""
Here is the step-by-step explanation of the solution:

1. Define a function named pair_xor_Sum which takes two parameters: