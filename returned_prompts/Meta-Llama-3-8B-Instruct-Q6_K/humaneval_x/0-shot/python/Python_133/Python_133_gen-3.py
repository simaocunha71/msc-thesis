```
def sum_squares(lst):
    return sum(math.ceil(i)**2 for i in lst)
```
The function sum_squares takes a list of numbers as input, and returns the sum of the squares of the numbers in the list. Each number in the list is rounded up to the nearest integer using the math.ceil function before squaring. The sum of these squared numbers is then returned. The ** operator is used to square the numbers, and the sum function is used to add them up. The for loop is a generator expression that iterates over the numbers in the list, applies the math.ceil function to each number, squares the result, and adds it to the total sum.