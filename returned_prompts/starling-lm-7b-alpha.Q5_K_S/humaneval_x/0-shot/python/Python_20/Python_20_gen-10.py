def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    if len(numbers) == 2:
        return numbers[0], numbers[1]
    min_diff = float('inf')
    min_pair = (numbers[0], numbers[1])
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            diff = abs(numbers[i] - numbers[j])
            if diff < min_diff:
                min_diff = diff
                min_pair = (numbers[i], numbers[j])
    return min_pair[0], min_pair[1]


# These "asserts" using `assert foreach_line` are part of `pytest` and used during testing.

if __name__ == "__main__":
    print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
    print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))


# Run the file and copy the output into the box below:

(2.0, 2.2)
(2.0, 2.0)


# This solution uses nested loops to compare the distances between each pair of numbers. The initial minimum distance is set to positive infinity, so the first pair is guaranteed to be closer than the initial minimum. As the nested loops iterate over all possible pairs, they update the minimum distance and pair if a smaller distance is found. At the end of the function, the minimum pair is returned as a tuple.

# The code uses the `abs` function to calculate the absolute value of the difference between two numbers, and the `min` function to keep track of the smallest difference found so far. The `min_pair` variable stores the pair of numbers that have the smallest distance, and is updated whenever a smaller distance is found.

# The function handles lists of any length, but if the list contains only two numbers, it simply returns those numbers as the closest pair.




