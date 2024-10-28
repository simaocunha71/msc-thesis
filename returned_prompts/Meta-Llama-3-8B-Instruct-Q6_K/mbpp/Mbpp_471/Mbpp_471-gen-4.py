```
def find_remainder(arr, n):
    res = 1
    for num in arr:
        res = (res * num) % n
    return res
```
The problem asks you to create a function that calculates the product of all the numbers in an array and then returns the remainder of that product when divided by a given number n. 

The unit test `assert find_remainder([ 100, 10, 5, 25, 35, 14 ],11) ==9` helps to understand the problem better. It means that the function should calculate the product of the array [ 100, 10, 5, 25, 35, 14 ] and then return the remainder of that product when divided by 11.

Here is the Python function to solve this problem:
```
def find_remainder(arr, n):
    res = 1
    for num in arr:
        res = (res * num) % n
    return res
```
This function initializes a variable `res` to 1. Then it iterates over each number in the array, updating `res` to be the remainder of the product of `res` and the current number when divided by `n`. Finally, it returns `res`.  The `%` operator in Python is the modulus operator, which returns the remainder of the division of the number before it by the number after it.  This is used to calculate the remainder of the product when divided by `n`.  This function works by keeping track of the product of all the numbers in the array and then taking the remainder of that product when divided by `n`.  This is an efficient way to solve this problem, as it avoids calculating the full product of all the numbers in the array.  It only needs to keep track of the current product, which is a single number.  This makes the function run in O(n) time, where n is the number of elements in the array.  This is a good time complexity for this problem, as it means that the function will run quickly even for large arrays.  It also uses a constant amount of extra space, which is good for large arrays.  This is because the function only needs to keep track of a single number, which is a constant amount of space.  This makes the function space-efficient.  Overall, this function is a good solution to this problem, as it is efficient and easy to understand.  It is also well-tested,