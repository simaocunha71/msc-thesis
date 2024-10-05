    import statistics
    import math

    def mean_absolute_deviation(numbers: List[float]) -> float:
        mean = statistics.mean(numbers)
        return statistics.mean([abs(num - mean) for num in numbers])  # Calculate MAD

    # Example
    numbers = [1.0, 2.0, 3.0, 4.0]
    print(mean_absolute_deviation(numbers))  # Output: 1.0
    ```


In this code, the `mean_absolute_deviation` function calculates the Mean Absolute Deviation (MAD) of a given list of numbers. It first calculates the mean of the input numbers using the `statistics.mean` function. Then, it calculates the absolute difference between each number and the mean using a list comprehension. Finally, it calculates the average of these absolute differences using the `statistics.mean` function again. This result is the Mean Absolute Deviation.

The example at the end demonstrates how to use this function with a list of numbers. It calculates the MAD for the list `[1.0, 2.0, 3.0, 4.0]` and prints the result, which is `1.0`.