```
def prod_signs(arr):
    if not arr:
        return None
    prod = 1
    sum_mag = 0
    for num in arr:
        if num == 0:
            return 0
        sum_mag += abs(num)
        prod *= -1 if num < 0 else 1
    return sum_mag * prod
```


Explanation:
1. If the array is empty, return None.
2. Initialize prod (product of signs) to 1 and sum_mag (sum of magnitudes) to 0.
3. Iterate over the array. For each number:
   - If the number is 0, return 0 (since multiplying by 0 will result in 0).
   - Add the absolute value of the number to sum_mag.
   - Multiply prod by -1 if the number is negative, else multiply by 1 (to update the product of signs).
4. Return the product of sum_mag and prod.
5. This solution has a time complexity of O(n), where n is the length of the array, since we're iterating over the array once. The space complexity is O(1), as we're using a constant amount of space.