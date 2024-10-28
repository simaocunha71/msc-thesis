```
def count_nums(arr):
    return sum(1 for x in arr if sum(int(digit) for digit in str(abs(x))) > 0)
```


The function count_nums takes an array of integers and returns the number of elements which has a sum of digits > 0. 

The expression `sum(1 for x in arr if sum(int(digit) for digit in str(abs(x))) > 0)` iterates over each element in the array. For each element, it converts the element to its absolute value (to handle negative numbers) and then calculates the sum of its digits. If the sum of the digits is greater than 0, it counts this element. The sum of these counts is the number of elements which has a sum of digits > 0. 

The time complexity of this function is O(n*m), where n is the number of elements in the array and m is the maximum number of digits in an element. The space complexity is O(n), for the list comprehension. 





The function `count_nums` can also be written as follows:

```
def count_nums(arr):
    return sum(1 for x in arr if sum(int(digit) for digit in str(abs(x))) > 0)
```


This function works similarly to the previous one. It uses a generator expression to iterate over each element in the array, convert it to its absolute value, calculate the sum of its digits, and count the elements with a sum of digits greater than 0. The sum of these counts is the number of elements which has a sum of digits > 0. 

This function also has a time complexity of O(n*m) and a space complexity of O(n), where n is the number of elements in the array and m is the maximum number of digits in an element. 





The function `count_nums` can also be written as follows:

```
def count_nums(arr):
    return sum(1 for x in arr if sum(int(digit) for digit in str(abs(x))) > 0)
```


This function works similarly to the previous ones. It uses a generator expression to iterate over each element in the array, convert it to its absolute value, calculate the sum of its digits, and count the elements with a sum of digits greater than 0. The sum of these counts is the number of elements which has a sum of digits > 0. 

This function also has a time complexity of O(n*m) and a space complexity of O(n