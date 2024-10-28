```
def by_length(arr):
    if not arr:
        return []
    arr = sorted([i for i in arr if 1 <= i <= 9])
    arr = arr[::-1]
    names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return [names[i-1] for i in arr]
```



This code first checks if the input array is empty. If it is, it returns an empty array. 

Then it creates a new list with only the numbers in the range 1-9. It sorts this list and then reverses it. 

Next, it creates a list of names corresponding to the numbers from 1 to 9. 

Finally, it creates a new list by looking up each number in the reversed list in the list of names and returns this new list. 

If the array contains any numbers outside the range 1-9, these numbers are ignored.  For example, if the array contains -1, this number will not be included in the output. 

If the array contains a number greater than 9, this number will also be ignored. For example, if the array contains 55, this number will not be included in the output.  The output will be a list of strings, where each string is the name of a number in the range 1-9.  If the input array is empty, the output will also be an empty array.  If the input array contains any numbers outside the range 1-9, the output will also contain only the names of numbers in the range 1-9.  If the input array contains only numbers outside the range 1-9, the output will be an empty array.  If the input array contains both numbers and numbers outside the range 1-9, the output will be a list of strings, where each string is the name of a number in the range 1-9.  If the input array contains multiple numbers that are the same, the output will contain the same number of occurrences of the corresponding name in the list of names.  For example, if the input array is [2, 2, 1, 1], the output will be ['Two', 'Two', 'One', 'One'].  If the input array is [2, 1, 1, 4, 5, 8, 2, 3], the output will