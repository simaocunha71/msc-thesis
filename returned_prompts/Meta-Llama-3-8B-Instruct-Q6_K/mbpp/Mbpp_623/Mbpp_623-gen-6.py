```
def nth_nums(lst, n):
    return [i ** n for i in lst]
```
This function takes a list of numbers and an integer n as input, and returns a new list where each number is the nth power of the corresponding number in the input list.

For example, if we call `nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)`, it will return `[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]`, which are the squares of the numbers in the input list.

The function uses a list comprehension to create the new list. The expression `i ** n` calculates the nth power of each number in the input list, and the list comprehension iterates over the input list and uses each number to create a new list element. The resulting list is then returned.