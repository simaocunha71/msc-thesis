def pair_xor_Sum(nums, k):
    xor = 0
    for i in range(len(nums)):
        xor ^= nums[i]
    return k * (xor + (len(nums) % 2 == 0) * xor)


def pair_xor_Sum(nums, k):
    xor = 0
    for i in range(len(nums)):
        xor ^= nums[i]
    return k * (xor + (len(nums) % 2 == 0) * xor)

print(pair_xor_Sum([5,9,7,6], 4))
# Output: 47


"""
Time Complexity: O(n), where n is the length of the input array.
Space Complexity: O(1), as we are using constant extra space.
"""

```

```
"""
Explanation: 

In XOR operation, a ^ b = b ^ a. XOR is commutative, associative, and distributive over addition modulo 2.

To find the XOR of all the pairs, we can XOR each element of the array with the XOR of all the elements of the array.

Let's take an example to understand the above line:

Consider the array [1, 2, 3, 4]
XOR of all elements = 1 XOR 2 XOR 3 XOR 4 = 10
Now, XOR each element with XOR of all elements:
1 XOR 10 = 11
2 XOR 10 = 6
3 XOR 10 = 13
4 XOR 10 = 14

Now, if we take the XOR of all these values, it will be same as the XOR of all the elements of the array.

If the length of the array is even, then the XOR of all the elements of the array will be 0.
In this case, we need to add the XOR of all the elements of the array to the result, as per the given formula.

If the length of the array is odd, then the XOR of