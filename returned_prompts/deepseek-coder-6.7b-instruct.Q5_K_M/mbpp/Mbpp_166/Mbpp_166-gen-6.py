
def find_even_pair(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] ^ nums[j] % 2 == 0:
                count += 1
    return count

print(find_even_pair([5, 4, 7, 2, 1]))

# Alternate solution

def find_even_pair_alt(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j]) % 2 == 0:
                count += 1
    return count

print(find_even_pair_alt([5, 4, 7, 2, 1]))

"""
The first solution checks the xor result of each pair of numbers in the list. If the xor result is even, it increases the pair count. 

The second solution checks the sum of each pair of numbers. If the sum is even, it increases the pair count. 

Both of these solutions have a time complexity of O(n^2) because they involve a nested loop.
"""
<jupyter_output>
4
4
<jupyter_text>
