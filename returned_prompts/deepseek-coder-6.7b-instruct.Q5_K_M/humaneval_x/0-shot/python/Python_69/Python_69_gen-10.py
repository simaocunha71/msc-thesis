
def search(lst):
    count = {}
    for num in lst:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    greatest = -1
    for num in sorted(count.keys(), reverse=True):
        if count[num] >= num:
            greatest = num
            break
    return greatest

print(search([4, 1, 2, 2, 3, 1])) # 2
print(search([1, 2, 2, 3, 3, 3, 4, 4, 4])) # 3
print(search([5, 5, 4, 4, 4])) # -1

Explanation:

In the function `search`, we first create a dictionary `count` where each key is an integer in the list and the value is the frequency of the integer in the list. 

Then, we sort the keys of the dictionary in descending order and iterate through them. If the frequency of the current integer is greater than or equal to the integer itself, we return the integer. 

If no such integer is found, we return `-1`.

This function works because it iterates through the integers in descending order of their frequency, so the first integer that satisfies the condition is the greatest one.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

# Test cases to validate the solution
lst = [4, 1, 2, 2, 3, 1]
print(search(lst)) # 2
lst = [1, 2, 2, 3, 3, 3, 4, 4, 4]
print(search(lst)) # 3
lst = [5, 5, 4, 4, 4]
print(search(lst)) # -1

# Test case with large input
import random
lst = [random.randint(1, 1000000) for _ in range(1000000)]
print(search(lst)) # It should return a number in the range