
The solution is:
```
def order_by_points(nums):
    return sorted((str(num), num) for num in nums, key=lambda x: (sum(int(digit) for digit in x[0]), nums.index(x[1])))
```
This function uses the built-in `sorted` function to sort the list of numbers based on the sum of their digits and then by their original index in the list. The key function used in the `sorted