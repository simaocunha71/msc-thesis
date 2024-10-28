```
def sum_to_n(n: int):
    return sum(range(1, n+1))
```
The function sum_to_n takes an integer n as input and returns the sum of all integers from 1 to n. The built-in Python function range generates a sequence of numbers from 1 to n (inclusive), and the built-in function sum adds up all the numbers in this sequence. For example, sum_to_n(30) returns 465, which is the sum of 1 + 2 + ... + 30. The unit tests provided in the problem check that the function works correctly for various values of n. 

Note that the range function in Python generates a sequence of numbers up to, but not including, the stop value. Therefore, we need to add 1 to n when calling range to include n in the sequence. For example, range(1, 5) generates the sequence 1, 2, 3, 4, while range(1, 6) generates the sequence 1, 2, 3, 4, 5. 

The function sum_to_n is a simple and efficient way to calculate the sum of all integers from 1 to n. It has a time complexity of O(n) and a space complexity of O(1), making it suitable for use in a wide range of applications. 