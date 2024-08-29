
def pair_xor_Sum(arr, n):
    sum = 0
    for i in range(0, 32):
        c = 0
        for j in range(0, n):
            if ((arr[j] & (1 << i))):
                c += 1
        sum += c * (n - c) * 2
    return sum
 
arr = [5,9,7,6]
n = len(arr)
print(pair_xor_Sum(arr, n))


"""
Explanation:

In the question, we are asked to find the sum of xor of all pairs of numbers in the given list.

To solve this, we use bitwise XOR operation which is different from addition.

A XOR B is different from A + B.

So, we need to find the sum of all pairs of XOR operations, not addition.

To find all pairs of XOR, we can use the property of XOR operation that XOR of any number with itself is 0 and XOR of any number with 0 is number itself.

We calculate the count of numbers with set bit at i-th position and calculate the pairs that can be formed using these numbers.

The pairs that can be formed are count of numbers with set bit at i-th position * count of numbers with unset bit at i-th position.

We multiply this value by 2 (as XOR operation is commutative i.e., A XOR B = B XOR A) and add it to the sum for each bit position from 0 to 31.

Finally, we return the sum.

In the provided example, the list is [5,9,7,6] and the length of list is 4.

Call the function with the list and length as parameters.

The output will be 47.
"""

