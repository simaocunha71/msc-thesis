
The problem asks to sort the integers between 1 and 9 inclusive, reverse the resulting array, and then replace each digit with its corresponding name. If the array is empty, return an empty array. If the array contains any numbers outside the range 1 to 9, ignore them.

Here is the Python solution:

```
def by_length(arr):
    names = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
    return [names[i] for i in sorted([i for i in arr if 1 <= i <= 9], reverse=True)]
```

This solution uses a dictionary to map the numbers to their corresponding names. It then uses a list comprehension to filter the array to only include numbers between 1 and 9, sorts the filtered array in reverse order, and finally replaces each digit with its corresponding name. If the array is empty, it will return an empty list. If the array contains any numbers outside the range 1 to 9, they will be ignored.