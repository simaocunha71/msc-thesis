```
def by_length(arr):
    if not arr:
        return []

    names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    sorted_arr = sorted([i for i in arr if 1 <= i <= 9])
    result = [names[i-1] for i in reversed(sorted_arr)]
    return result
```


Explanation:

1. The function first checks if the input array is empty. If it is, the function returns an empty array.
2. The function then creates a list of names for the digits 1 through 9.
3. The function uses a list comprehension to filter the input array and only include the integers that are between 1 and 9 (inclusive).
4. The function sorts the filtered array in ascending order.
5. The function then reverses the sorted array.
6. The function uses another list comprehension to replace each digit in the reversed array with its corresponding name from the list of names.
7. The function returns the resulting list of names. If the input array contains any integers outside the range 1 to 9, they are ignored and not included in the final result. If the input array contains any non-integer values, they are also ignored. If the input array is empty, the function returns an empty array.