```
def perfect_squares(start, end):
    return [i for i in range(start, end+1) if round(i**0.5)**2 == i]
```
This function generates all perfect squares between the given start and end numbers. It uses list comprehension to generate a list of numbers from start to end (inclusive), and then filters the list to include only the numbers that are perfect squares. The filtering is done by checking if the square root of the number is an integer (i.e., if the square root is equal to its integer part). This is done by rounding the square root and checking if the result squared is equal to the original number. If it is, then the number is a perfect square, and it is included in the output list.