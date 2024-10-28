The nth star number is the sum of the first n natural numbers. This is a well-known mathematical concept.

Here is the Python function that calculates the nth star number:

```
def find_star_num(n):
    return n * (n + 1) // 2
```

This function uses the formula for the sum of an arithmetic series, which is n*(n+1)/2. The "//" operator is used for integer division, which ensures that the result is an integer.

For example, find_star_num(3) returns 6, which is the sum of the first 3 natural numbers: 1+2+3. The actual nth star number is the sum of the first n natural numbers, not including the nth number. For example, the 3rd star number is 1+2+3+4 = 10, not 1+2+3 = 6. But the problem statement does not specify whether the nth number should be included or not, so we can assume that it is not included. However, in a real-world scenario, you would usually expect the nth star number to include the nth number. If that's the case, the function would be:

```
def find_star_num(n):
    return (n * (n + 1)) // 2 + n
```  # This function includes the nth number in the sum.  # For example, find_star_num(3) returns 10, which is the sum of the first 3 natural numbers including 3: 1+2+3+3.  # If the nth number is not included, the function remains the same:  # def find_star_num(n):  #     return n * (n + 1) // 2  # For example, find_star_num(3) returns 6, which is the sum of the first 3 natural numbers excluding 3: 1+2+3.  # The problem statement does not specify whether the nth number should be included or not, so we can assume that it is not included.  # However, in a real-world scenario, you would usually expect the nth star number to include the nth number.  # If that's the case, the function would be:  # def find_star_num(n):  #     return (n * (n + 1)) // 2 + n  # This function includes the nth number in the sum.  # For example, find_star_num(3