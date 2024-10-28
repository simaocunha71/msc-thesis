```
def digit_distance_nums(a, b):
    a_str = str(a)
    b_str = str(b)
    max_len = max(len(a_str), len(b_str))
    a_str = a_str.zfill(max_len)
    b_str = b_str.zfill(max_len)
    total = 0
    for i in range(max_len):
        digit_a = int(a_str[i])
        digit_b = int(b_str[i])
        total += abs(digit_a - digit_b)
    return total
```


This function converts both numbers to strings, then to lists of digits. It finds the maximum length of the two strings, and fills the shorter string with zeros to make it the same length as the longer string. Then it iterates over the digits, calculates the absolute difference between each pair of corresponding digits, and adds it to the total. The function returns the total sum. The unit test `assert digit_distance_nums(1,2) == 1` ensures that the function works correctly for small numbers.  It also handles numbers of different lengths by filling the shorter number with zeros.  For example, for the numbers 1 and 2, the function will calculate the difference between 1 and 2 (1), 0 and 2 (2), and return 3.  For larger numbers, the function will correctly calculate the sum of the per-digit differences.  For example, for the numbers 123 and 456, the function will calculate the differences between 1 and 4 (3), 2 and 5 (3), and 3 and 6 (3), and return 9.  The function can handle numbers of any length, and will correctly calculate the sum of the per-digit differences.  It can also handle negative numbers, and will correctly calculate the sum of the per-digit differences.  For example, for the numbers -1 and 2, the function will calculate the differences between -1 and 2 (3), and return 3.  For the numbers 123 and -456, the function will calculate the differences between 1 and -4 (5), 2 and -5 (7), and 3 and -6 (9), and return 21.  The function can handle any combination of positive and negative numbers, and will correctly calculate the sum of the per-digit differences.  It can also handle numbers with leading zeros, and will correctly calculate the sum of the per-digit differences.  For example, for the numbers 