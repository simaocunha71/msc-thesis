```
def armstrong_number(n):
    num_str = str(n)
    num_len = len(num_str)
    sum = 0
    for i in range(num_len):
        sum += int(num_str[i])**num_len
    return sum == n
```    
The function converts the given number into a string, calculates the length of the string, then calculates the sum of each digit raised to the power of the length. If the sum is equal to the original number, the function returns True, indicating that the number is an Armstrong number; otherwise, it returns False.

The unit test `assert armstrong_number(153)==True` ensures that the function correctly identifies 153 as an Armstrong number.