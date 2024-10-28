```
def sum_of_digits(lst):
    return sum(sum(int(digit) for digit in str(num)) for num in lst)
```
This function works by iterating over each number in the input list, converting it to a string, and then summing up the digits in that string. The sum of these sums is then returned. The unit test `assert sum_of_digits([10,2,56])==14` ensures that the function works correctly. 

The function works for the given unit test because the sum of digits of 10 is 1+0=1, the sum of digits of 2 is 2, and the sum of digits of 56 is 5+6=11, so the total sum is 1+2+11=14.  This is what the function returns.  It correctly handles the conversion of numbers to strings and the summing of the digits.  It also correctly handles the iteration over the input list.  So, the function is correct and passes the unit test. 