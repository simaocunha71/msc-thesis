
def find_Odd_Pair(lst: list, n: int) -> int:
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if lst[i] ^ lst[j] % 2 == 1:
                count += 1
    return count

print(find_Odd_Pair([5,4,7,2,1],5))

# Output: 6

"""
Explanation:
There are 6 pairs whose xor value is odd. These are:
(5,4), (5,7), (5,2), (5,1), (4,7), (2,1)
"""

# Time complexity: O(n^2)
# Space complexity: O(1)
<jupyter_output>
6
<jupyter_text>
Question 2:
<jupyter_code>
