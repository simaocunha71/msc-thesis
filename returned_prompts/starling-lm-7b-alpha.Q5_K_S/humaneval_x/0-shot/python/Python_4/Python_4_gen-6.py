    total = 0.0
    for x in numbers:
        total += abs(x - sum(numbers)/len(numbers))
    return total / len(numbers)


# Run tests
assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 1.0
assert mean_absolute_deviation([-1.0, 1.0, 3.0, 4.0]) == 2.0
assert mean_absolute_deviation([-1.0, -1.0, -1.0, -1.0]) == 0.0


A summary of our answer is:
To calculate the Mean Absolute Deviation (MAD), we subtract the mean from each element in the dataset, take the absolute value of the result, sum these absolute deviations, and then divide by the number of elements in the dataset.

Here's a step-by-step explanation of the solution:

1. Initialize a variable "total" to keep track of the sum of absolute deviations from the mean.
2. Iterate over each element in the input list of numbers.
3. For each number, subtract the mean (calculated as the sum of all numbers divided by the length of the dataset) from the current number.
4. Take the absolute value of the result from step 3.
5. Add the absolute value from step 4 to the "total" variable.
6. Repeat steps 3-5 for all numbers in the dataset.
7. Divide the "total" variable by the length of the dataset to get the mean absolute deviation.
8. Return the mean absolute deviation as the result.

The provided code demonstrates the implementation of the mean_absolute_deviation function, which follows the steps outlined above. The function takes a list of float numbers as input and returns the mean absolute deviation as a float value.

The function first initializes the "total" variable to keep track of the sum of absolute deviations from the mean. It then iterates over each element in the input list of numbers. For each number, it subtracts the mean (calculated as the sum of all numbers divided by the length of the dataset) from the current number. It takes