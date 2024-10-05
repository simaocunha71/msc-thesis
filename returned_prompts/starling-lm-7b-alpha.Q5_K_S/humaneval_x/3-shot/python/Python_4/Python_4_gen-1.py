    def mean(numbers: List[float]) -> float:
        """ Calculate the mean of the given list of numbers
        >>> mean([1.0, 2.0, 3.0, 4.0])
        2.5
        """
        return sum(numbers) / len(numbers)

    def mean_absolute_deviation_helper(numbers: List[float]) -> float:
        mean_number = mean(numbers)
        result = 0.0
        for elem in numbers:
            result += abs(elem - mean_number)
        return result / len(numbers)

    return mean_absolute_deviation_helper(numbers)


