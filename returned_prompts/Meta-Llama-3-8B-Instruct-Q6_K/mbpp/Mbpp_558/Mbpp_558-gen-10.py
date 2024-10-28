```
def digit_distance_nums(a, b):
    max_num = max(a, b)
    min_num = min(a, b)
    return sum(abs(int(digit) - int(digit2)) for digit, digit2 in zip(str(max_num), str(min_num)))
```


The problem is asking to find the sum of the per-digit difference between two integers. For example, if the two integers are 12 and 25, the per-digit difference would be |1-2| + |2-5| = 1 + 3 = 4.

Here is the Python function that solves this problem:

```
def digit_distance_nums(a, b):
    max_num = max(a, b)
    min_num = min(a, b)
    return sum(abs(int(digit) - int(digit2)) for digit, digit2 in zip(str(max_num), str(min_num)))
```

This function works by first finding the maximum and minimum of the two input integers. It then converts the maximum integer to a string and iterates over each character (digit) in the string. For each digit, it finds the corresponding digit in the minimum integer by using the zip function, converts each digit to an integer, and calculates the absolute difference between the two digits. The sum of these differences is then returned.

For example, if the input is 12 and 25, the function would first find the maximum and minimum as 25 and 12, respectively. It would then convert 25 to the string '25' and iterate over each character in the string, which would be '2' and '5'. For each digit, it would find the corresponding digit in 12 (which is also '2' and '5'), convert each digit to an integer, and calculate the absolute difference between the two digits, which would be |2-2| + |5-5| = 0 + 0 = 0. The sum of these differences would be 0, which is the correct result.