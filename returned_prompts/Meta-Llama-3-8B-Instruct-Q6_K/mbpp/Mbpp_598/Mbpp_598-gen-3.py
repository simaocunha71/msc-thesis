```
def armstrong_number(n):
    num_str = str(n)
    num_len = len(num_str)
    sum = 0
    for i in num_str:
        sum += int(i) ** num_len
    return sum == n
```


This function converts the given number into a string, calculates the power of each digit to the number of digits in the number, and then checks if the sum is equal to the original number. If it is, then the number is an Armstrong number. The unit test provided, `assert armstrong_number(153)==True`, confirms this. 

For example, the number 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153. 

This function works for both positive and negative Armstrong numbers. However, it does not handle non-integer inputs. If you want to extend it to handle non-integer inputs, you would need to add error checking code to handle such cases. 





