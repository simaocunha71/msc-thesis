To solve this problem, you can follow these steps:

1. Sort the given list of numbers in ascending order.
2. Initialize two variables, one for the closest pair of elements and one for the minimum distance between them.
3. Iterate through the sorted list, comparing the distances between adjacent elements.
4. If the distance between the current pair of elements is less than the previously calculated minimum distance, update the variables to reflect the new closest pair and minimum distance.
5. After iterating through the entire list, return the closest pair of elements.

Here's a Python implementation of the solution:

```python
def findClosestElements(numbers):
    # Sort the given list of numbers in ascending order
    numbers.sort()

    # Initialize variables for the closest pair and minimum distance
    closest_pair = (numbers[0], numbers[1])
    min_distance = abs(closest_pair[0] - closest_pair[1])

    # Iterate through the sorted list, comparing distances between adjacent elements
    for i in range(len(numbers) - 1):
        distance = abs(numbers[i] - numbers[i+1])

        # If the distance between the current pair of elements is less than the previously calculated minimum distance, update the variables
        if distance < min_distance:
            min_distance = distance
            closest_pair = (numbers[i], numbers[i+1])

    # Return the closest pair of elements
    return closest_pair
```

You can test the function with the provided test cases:

```python
print(findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # (2.0, 2.2)
print(findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # (2.0, 2.0)
```

The function will return the closest pair of elements in ascending order, as specified in the problem statement.

Note: It's worth mentioning that the problem statement mentions a supplied "list of numbers," but