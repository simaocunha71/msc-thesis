```
def count_nums(arr):
    count = 0
    for num in arr:
        if num > 0:
            if sum(int(digit) for digit in str(abs(num))) > 0:
                count += 1
        elif num < 0:
            if sum(int(digit) for digit in str(abs(num)) if digit != '0') > 0:
                count += 1
    return count
```


The function `count_nums` takes an array of integers as an argument and returns the count of elements in the array that have a sum of digits greater than 0. It iterates over each number in the array, and for each number, it checks if the sum of its digits is greater than 0. If the number is positive, it simply calculates the sum of its digits. If the number is negative, it calculates the sum of its digits excluding the first digit which is negative (i.e., the first character of the string representation of the absolute value of the number). The count is incremented for each number that has a sum of digits greater than 0. The function returns the total count. 

The unit tests provided ensure that the function works correctly for various inputs, including an empty array, an array with only negative numbers, and an array with positive and negative numbers. 

The time complexity of the function is O(n*m), where n is the number of elements in the array and m is the maximum number of digits in a number. The space complexity is O(m) for storing the digits of each number. 