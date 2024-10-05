def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    closest_pair = (numbers[0], numbers[1])
    smallest_difference = numbers[1] - numbers[0]
    for i in range(2, len(numbers)):
        difference = numbers[i] - numbers[i - 1]
        if difference < smallest_difference:
            closest_pair = (numbers[i - 1], numbers[i])
            smallest_difference = difference
    return closest_pair


print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))

This code first sorts the list of numbers. It then initializes the closest pair of numbers and the smallest difference found so far. It iterates through the sorted list of numbers, keeping track of the pair with the smallest difference. Finally, it returns the pair of numbers with the smallest difference.

In the first example, the pair (2.0, 2.2) is returned because 2.2 is the smallest number in the list that is larger than 2.0.

In the second example, the pair (2.0, 2.0) is returned because there are two 2.0s in the list and they are the closest to each other.
<jupyter_text>
Question 3
<jupyter_code>
