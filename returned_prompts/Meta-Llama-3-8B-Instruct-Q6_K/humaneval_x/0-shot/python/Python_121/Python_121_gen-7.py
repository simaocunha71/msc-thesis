    # Initialize the sum variable to 0
    total_sum = 0

    # Iterate over the list with enumerate to get both index and value
    for i, num in enumerate(lst):
        # Check if the index is even (i.e., in an even position)
        if i % 2 == 0:
            # Check if the number is odd
            if num % 2 != 0:
                # Add the odd number to the sum
                total_sum += num

    # Return the sum of the odd elements in even positions
    return total_sum
```


Example inputs and outputs:
```
print(solution([5, 8, 7, 1]))  # Output: 12
print(solution([3, 3, 3, 3, 3]))  # Output: 9
print(solution([30, 13, 24, 321]))  # Output: 0
```


Explanation:
- The function takes a list of integers as input.
- It initializes a variable `total_sum` to 0, which will be used to store the sum of the odd elements in even positions.
- It iterates over the list using `enumerate`, which returns both the index `i` and the value `num` of each element in the list.
- For each element, it checks if the index `i` is even (i.e., in an even position) using the modulo operator (`i % 2 == 0`).
- If the index is even, it checks if the number `num` is odd by using the modulo operator (`num % 2 != 0`).
- If the number is odd and in an even position, it adds the number to `total_sum`.
- Finally, it returns the sum of the odd elements in even positions.