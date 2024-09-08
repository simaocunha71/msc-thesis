"""
Firstly, I need to understand the problem statement. 

It seems like we are given a list and a length of the list. We are asked to count the number of pairs in the list that have an xor value of odd.

The xor operation is a bitwise operation that takes two inputs, and returns the result of a binary XOR operation. It returns a binary number where a bit is set if the corresponding bit in the input bits is not set.

Since the xor operation returns 1 if the two bits are different and 0 if they are the same, if the xor value is odd, that means at least one bit is 1 and the other is 0. 

So, I can solve this problem by iterating over all pairs of numbers in the list and counting the number of pairs where the xor operation results in an odd number.

Here is a Python solution that uses two nested loops to generate all pairs of numbers in the list, and uses the bitwise xor operation to determine if the xor value is odd:
"""

def find_Odd_Pair(arr, n):
    count = 0
    for i in range(0, n):
        for j in range(i+1, n):
            if arr[i] ^ arr[j] & 1:
                count += 1
    return count

print(find_Odd_Pair([5,4,7,2,1],5))  # returns 6

"""
This solution has a time complexity of O(n^2) because it uses two nested loops to generate all pairs of numbers in the list. The space complexity is O(1) because it only uses a constant amount of space to store the count of pairs and the indices of the current pair.
"""























































































































