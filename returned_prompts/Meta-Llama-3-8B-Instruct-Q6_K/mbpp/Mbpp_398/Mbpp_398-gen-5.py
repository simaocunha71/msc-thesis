```
def sum_of_digits(lst):
    return sum(sum(int(i) for i in str(n)) for n in lst)
```


This function works by iterating over each number in the list, converting the number to a string, and then summing up the digits in the string. It then sums up these sums to get the total sum of digits. The unit test `assert sum_of_digits([10,2,56])==14` confirms that this function works correctly. 

For example, for the number 10, the function converts it to a string "10", then sums up the digits 1 and 0 to get 1. For the number 2, it converts it to a string "2", then sums up the digit 2 to get 2. For the number 56, it converts it to a string "56", then sums up the digits 5 and 6 to get 11. The function then sums up these sums to get 1 + 2 + 11 = 14. 

Note: This function assumes that the input list contains only integers. If the list can contain other types of numbers (like floats), the function would need to be modified to handle these cases. 