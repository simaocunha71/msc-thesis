```
def round_and_sum(numbers):
    rounded_numbers = [round(num) for num in numbers]
    total_sum = sum(rounded_numbers)
    return total_sum * len(rounded_numbers)
```


This function takes a list of numbers as input, rounds each number to the nearest integer using the built-in round function, calculates the total sum of the rounded numbers using the built-in sum function, and then returns the total sum multiplied by the length of the list. The unit test `assert round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])==243` confirms that this function works as expected.