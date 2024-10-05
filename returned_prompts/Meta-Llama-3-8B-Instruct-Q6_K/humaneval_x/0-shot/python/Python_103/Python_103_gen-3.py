```
def rounded_avg(n, m):
    if n > m:
        return -1
    total = sum(range(n, m+1))
    avg = round(total / (m - n + 1))
    return bin(avg)[2:]
```


Explanation:
The function first checks if n is greater than m, and if so, returns -1.
If n is less than or equal to m, it calculates the total sum of the numbers from n to m (inclusive) using the built-in sum function and the range function.
The average is then calculated by dividing the total sum by the number of numbers (m - n + 1).
The average is rounded to the nearest integer using the round function.
Finally, the function converts the rounded average to binary using the bin function and returns the result as a string. The [2:] is used to remove the '0b' prefix that the bin function adds.