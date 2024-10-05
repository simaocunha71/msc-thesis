```
def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10 and str(num)[0] in '13579' and str(num)[-1] in '13579':
            count += 1
    return count
```


Explanation:
- We initialize a counter `count` to 0.
- We iterate over each number `num` in the input array `nums`.
- For each number, we check two conditions:
  - `num > 10`: The number is greater than 10.
  - `str(num)[0] in '13579' and str(num)[-1] in '13579'`: The first and last digits of the number are odd.
  - If both conditions are true, we increment the counter `count` by 1.
- Finally, we return the total count of numbers that meet the conditions.