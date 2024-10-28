You can solve this problem by creating a set to store the numbers in the list and then iterating over the set to find the pairs that XOR to an even number. Here is the Python solution:

```Python
def find_even_pair(nums):
    num_set = set(nums)
    count = 0
    for num in num_set:
        complement = num ^ (num - 1)
        count += num_set.count(complement)
    return count // 2
```

This function works by iterating over each number in the set and calculating its complement for XOR operation. It then counts the occurrences of the complement in the set and adds it to the total count. The `// 2` at the end is to divide the count by 2 because each pair is counted twice. The time complexity of this function is O(n) where n is the length of the input list. The space complexity is O(n) as well due to the set used to store the numbers. 

The unit test `assert find_even_pair([5, 4, 7, 2, 1]) == 4` is used to verify the correctness of the function. It checks if the function returns 4 for the given list of numbers. The function should pass this test if it is implemented correctly. 