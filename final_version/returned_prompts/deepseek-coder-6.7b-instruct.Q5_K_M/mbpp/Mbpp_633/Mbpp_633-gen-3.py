def pair_xor_Sum(lst, n):
    xor_sum = 0
    for i in range(n):
        for j in range(i+1, n):
            xor_sum += lst[i] ^ lst[j]
    return xor_sum

print(pair_xor_Sum([5,9,7,6],4)) # 47

Explanation:
The function works by iterating over each pair of elements in the list. For each pair, it computes the XOR of the two elements and adds this value to a running total. The XOR operation is performed using the caret symbol (^). The total of these XOR operations is then returned as the result.

This function works with any list of integers and any number of elements in the list. However, it assumes that the list and the number of elements are provided correctly. If the list does not contain the specified number of elements, or if the elements in the list are not integers, the function may not behave as expected.
"""

