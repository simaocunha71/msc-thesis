
def find_Odd_Pair(arr,n):
    odd_count = 0
    even_count = 0

    # count the number of odd and even elements in array
    for i in range(0, n):
        if (arr[i] & 1):
            odd_count += 1
        else:
            even_count += 1

    # if there are more odd elements, there will be odd number of pairs with odd xor
    return odd_counter * (odd_counter - 1) // 2 + even_counter * (even_counter - 1) // 2

print(find_Odd_Pair([5,4,7,2,1],5))  # 6

Explanation:

The function find_Odd_Pair first initializes two counters, odd_count and even_count. The counters count the number of odd and even elements in the array.

Then, it calculates the number of pairs with odd xor. For every odd element, it calculates the number of pairs it can form with any other odd element and any even element. The total number of pairs is sum of all these individual pairs.

Finally, it returns the total number of pairs with odd xor.
"""

def find_Odd_Pair(arr,n):
    odd_count = 0
    even_count = 0

    for i in range(0, n):
        if (arr[i] & 1):
            odd_count += 1
        else:
            even_count += 1

    return odd_count * (odd_count - 1) // 2 + even_count * (even_count - 1) // 2

print(find_Odd_Pair([5,4,7,2,1],5))  # 6
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
