def count_same_pair(l1, l2):
    count = 0
    for i in range(len(l1)):
        if l1[i] == l2[i]:
            count += 1
    return count

print(count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9]))

"""
In this solution, we define a function count_same_pair that takes two lists as input. We initialize a count variable to 0. We then run a for loop that goes through each index in the lists. If the value at the current index in the two lists is the same, we increment the count by 1. Finally, we return the count.
"""

# Test case:
assert count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9])==4
<jupyter_output>
4
<jupyter_text>
Explanation: The indices where the values are same are at 0th, 2nd, 3rd, and 4th positions in the given lists. So, the function returns 4.  Question 3:Write a function that takes a string and returns the string with all words reversed in place. Do not use any built-in functions to reverse the string or list.
<jupyter_code>
