```
def rounded_avg(n, m):
    if n > m:
        return -1
    avg = (n + m) // 2
    return bin(round(avg))[2:]
```


Explanation:
This function first checks if n is greater than m. If it is, the function returns -1. 
Then, it calculates the average of the integers from n through m using integer division. 
The round function is used to round the average to the nearest integer. 
Finally, the bin function is used to convert the rounded average to binary, and the result is sliced to remove the "0b" prefix. 
The function returns the binary representation of the rounded average. 