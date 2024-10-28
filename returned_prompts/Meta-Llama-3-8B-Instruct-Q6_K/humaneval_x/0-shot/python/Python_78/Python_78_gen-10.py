```
def hex_key(num):
    hex_to_dec = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    prime_hex = ['2', '3', '5', '7', 'B', 'D']
    count = 0
    for char in num:
        if char in prime_hex:
            count += 1
    return count
```


This function first defines a dictionary to convert hexadecimal digits to decimal numbers. Then it defines a list of hexadecimal digits that are prime numbers. It initializes a count to zero, then it iterates over each character in the input string. If the character is in the list of prime hexadecimal digits, it increments the count. Finally, it returns the count. 

For example, if the input is "AB", the function will return 1 because 'B' is the only prime hexadecimal digit. If the input is "1077E", the function will return 2 because '1', '7', and '7' are prime hexadecimal digits. If the input is "ABED1A33", the function will return 4 because 'B', 'D', '1', and '3' are prime hexadecimal digits. If the input is "123456789ABCDEF0", the function will return 6 because '1', '2', '3', '5', '7', 'B', 'D', and 'F' are prime hexadecimal digits. If the input is "2020", the function will return 2 because '2' and '0' are prime hexadecimal digits. 





Final Answer: The final answer is the function above. I hope it is correct.