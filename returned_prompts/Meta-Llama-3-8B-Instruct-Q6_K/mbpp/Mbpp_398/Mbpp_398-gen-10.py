```
def sum_of_digits(lst):
    return sum(sum(int(i) for i in str(n)) for n in lst)
```
The problem is asking to create a function that takes a list of numbers as input and returns the sum of the digits of each number in the list. For example, if the input list is [10, 2, 56], the output should be 1+0+2+5+6 = 14.

The unit test `assert sum_of_digits([10,2,56])==14` helps to clarify the problem.

The solution uses a generator expression to convert each number in the list to a string, then to iterate over each character in the string, convert it back to an integer, and sum them up. The outer `sum` function is used to sum up these sums for each number in the list. 

For example, for the number 10, it converts it to the string '10', then to the list ['1', '0'], then sums up the integers 1 and 0, resulting in 1. For the number 2, it converts it to the string '2', then to the list ['2'], then sums up the integer 2, resulting in 2. For the number 56, it converts it to the string '56', then to the list ['5', '6'], then sums up the integers 5 and 6, resulting in 11. The outer `sum` function then sums up these sums, resulting in 1+2+11 = 14. 

This solution is concise and efficient, and it uses the `sum` function to simplify the code. 