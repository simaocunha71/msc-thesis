```
def number_ctr(s):
    count = 0
    for char in s:
        if char.isdigit():
            count += 1
    return count
````
The function `number_ctr` iterates over each character in the given string `s`. If the character is a digit (checked using the `isdigit` method), it increments the `count` variable. At the end of the function, it returns the total count of digits in the string. The unit test `assert number_ctr('program2bedone') == 1` ensures that the function works correctly. It checks if the function returns 1 when the input is 'program2bedone', which contains one digit '2'. 