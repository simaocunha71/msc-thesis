
def find_Odd_Pair(lst: list, n: int) -> int:
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if lst[i] ^ lst[j] & 1:
                count += 1
    return count

print(find_Odd_Pair([5,4,7,2,1],5))


"""
Explanation:

The function find_Odd_Pair takes a list and its length as input and returns the number of pairs whose xor value is odd.

The inner loop starts from i+1 because we don't want to compare an element with itself or with an element that comes before it.

The if condition checks if the xor of the two numbers is odd or not.

If the xor is odd, then we increment the count variable.

Finally, we return the count.
"""

# Time complexity: O(n^2)
# Space complexity: O(1)

# Solution 2: Using Bit Manipulation

def find_Odd_Pair(lst: list, n: int) -> int:
    count = 0
    for i in range(32):
        c = 0
        for j in range(n):
            if (lst[j] >> i) & 1:
                c += 1
        count += c * (n - c) * 2
    return count

print(find_Odd_Pair([5,4,7,2,1],5))


"""
Explanation:

The function find_Odd_Pair takes a list and its length as input and returns the number of pairs whose xor value is odd.

The outer loop runs 32 times as we are checking each bit of all the numbers.

The inner loop counts the number of numbers having the bit set to 1 for the ith bit position.

The count += c * (n - c) * 2 line calculates the number of pairs having the bit set to 1 for the ith bit position.

Finally, we return the count.
"""

# Time complexity: O(n)
# Space complexity: O