"""
def find_Odd_Pair(arr, n):
    count = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            if ((arr[i] ^ arr[j]) & 1):
                count += 1
    return count
print(find_Odd_Pair([5,4,7,2,1],5))
"""

O:
6

E:
The function "find_Odd_Pair" is taking an array and its length as input and returns the count of pairs whose xor value is odd.
The xor operation is a bitwise operator that gives 1 if the two bits are opposite, else it gives 0. So if the xor of two numbers gives 1, it means the xor value is odd.
The inner loop starts from i+1 because we are pairing every element with the elements that come after it.
The outer loop runs from 0 to n-1.
The function then checks every pair of numbers in the array and if the xor of the two numbers gives 1, it increments the count.
Finally, it returns the count.
"""
"""

T:
"""
The time complexity of this function is O(n^2).
Since there are two nested loops, one running from 0 to n and the other running from i+1 to n, the time complexity becomes O(n^2).
"""
"""

S:
"""
The space complexity of this function is O(1).
As no extra space is being used, the space complexity remains constant, i.e., O(1).
"""
"""

def find_Odd_Pair(arr, n):
    count = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            if ((arr[i] ^ arr[j]) & 1):
                count += 1
    return count

assert find_Odd_Pair([5,4,7,2,1],5) == 6, 'Test case 1 failed'
assert find_Odd_Pair([1, 2, 3, 4], 4) == 4, 'Test case 2 failed'
assert find_Odd_Pair([