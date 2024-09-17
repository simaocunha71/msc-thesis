```
def cube_nums(lst):
    return [i**3 for i in lst]
```


The problem is asking to create a function that takes a list of numbers and returns a new list containing the cube of each number in the original list.

The unit test provided is `assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]`, which helps clarify the problem by showing the expected output for a specific input.

The solution uses a list comprehension to iterate over the input list, cube each number, and add the result to the output list. The `**` operator is used to raise each number to the power of 3, effectively cubing it.

For example, if the input list is `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, the function will return `[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]`. This is the expected output according to the unit test.