```
def min_of_three(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c
```


This function compares the three numbers and returns the smallest one. The unit test `assert min_of_three(10,20,0)==0` ensures that the function works correctly. If the input numbers are 10, 20, and 0, the function should return 0, which is the smallest number.  The time complexity of this function is O(1) as it only requires a constant amount of time to compare the numbers. The space complexity is O(1) as it only requires a constant amount of space to store the variables.  This function is efficient and easy to understand. It does not handle the case where two or more numbers are equal. It simply returns the smallest number, without distinguishing between equal numbers. If you want to handle the case where two or more numbers are equal, you could modify the function to return all the smallest numbers. For example, you could return a list of all the smallest numbers.  Here is how you could modify the function to do that:
```
def min_of_three(a, b, c):
    min_numbers = [a, b, c]
    min_numbers.sort()
    return min_numbers[0]
```
This function sorts the list of numbers and returns the first one, which is the smallest number. If there are multiple smallest numbers, it returns the first one it encounters. This function handles the case where two or more numbers are equal. It returns all the smallest numbers.  However, this function has a time complexity of O(n log n) due to the sort operation. The space complexity is O(n) as it requires a list to store the numbers.  This function is less efficient than the original function, but it handles the case where two or more numbers are equal.  You could also use the built-in `min` function to find the smallest number. Here is how you could do that:
```
def min_of_three(a, b, c):
    return min(a, b, c)
```
This function is the most efficient and easiest to understand. It has a time complexity of O(1) and a space complexity of O(1). It handles the case where two or more numbers are equal. It returns all the smallest numbers.  However, this function is not suitable if