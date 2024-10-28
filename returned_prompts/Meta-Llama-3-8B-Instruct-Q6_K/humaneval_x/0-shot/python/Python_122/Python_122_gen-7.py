```
def add_elements(arr, k):
    total_sum = 0
    for num in arr[:k]:
        if len(str(abs(num))) <= 2:
            total_sum += num
    return total_sum
```
This function iterates over the first k elements of the array. For each element, it checks if the absolute value of the element (to handle negative numbers) as a string has a length of 2 or less. If it does, it adds the element to the total sum. Finally, it returns the total sum. 

For example, if `arr = [111,21,3,4000,5,6,7,8,9]` and `k = 4`, the function will iterate over the first 4 elements: `111`, `21`, `3`, and `4000`. It will add `21` and `3` to the total sum because their absolute values as strings have a length of 2 or less. The total sum will be `24`, which is the correct output. 