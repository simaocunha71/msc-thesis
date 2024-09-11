def diff_even_odd(nums):
    even, odd = [], []
    for i in nums:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even[0] - odd[0] if len(odd) > 0 and len(even) > 0 else None

# Test
print(diff_even_odd([1,3,5,7,4,1,6,8]))











"""
The above code returns the difference between the first even and first odd number in the given list.

Here's how the code works:

1. The function `diff_even_odd` takes a list `nums` as input.
2. It initializes two empty lists `even` and `odd` to store the even and odd numbers respectively.
3. It iterates over each number in the `nums` list.
4. If the number is divisible by 2 (i.e., even), it appends it to the `even` list.
5. If the number is not divisible by 2 (i.e., odd), it appends it to the `odd` list.
6. After iterating through all the numbers, it checks if both the `odd` and `even` lists have at least one element.
7. If both lists have at least one element, it calculates the difference between the first even and first odd number and returns the result.
8. If either the `odd` or `even` list is empty, it returns `None` to indicate that the difference cannot be calculated.
9. Finally, the function is tested with the given list `[1,3,5,7,4,1,6,8]` and the expected output `3` is printed.

Overall, the function efficiently finds the difference between the first even and first odd number in a given list, handling cases where one or both lists are empty.
"""

























































