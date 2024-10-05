```
def even_odd_count(num):
    num = abs(num)  # to handle negative numbers
    even_count = 0
    odd_count = 0

    for digit in str(num):
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return (even_count, odd_count)
```


Example:
even_odd_count(-12) returns (1, 1) 
even_odd_count(123) returns (1, 2) 
even_odd_count(555) returns (0, 3) 

Explanation: 
This function converts the input number into a string, then iterates over each character (digit) in the string. It checks if the digit is even (by checking if it's divisible by 2) and increments the corresponding count. Finally, it returns a tuple with the counts of even and odd digits. 

The use of abs(num) is to handle negative numbers. For negative numbers, the function will count the digits as if the number were positive. For example, even_odd_count(-12) will count the 1 and 2 as even and odd digits respectively, just like even_odd_count(12). 

The use of int(digit) is to convert each character (digit) in the string back to an integer, so that we can check if it's even or odd. 





This solution has a time complexity of O(n), where n is the number of digits in the input number. This is because we are iterating over each digit in the input number once. The space complexity is O(1), as we are using a constant amount of space to store the counts of even and odd digits. 