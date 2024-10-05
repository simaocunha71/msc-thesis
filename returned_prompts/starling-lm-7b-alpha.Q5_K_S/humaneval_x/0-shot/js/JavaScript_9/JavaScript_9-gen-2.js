To solve this problem, we can use a deque (double-ended queue) from the Python collections module to keep track of the maximum numbers found until the given moment. We can use the appendleft() function to add elements to the beginning of the deque, and the pop() function to remove the maximum number from the end of the deque.

Here's a step-by-step breakdown of the solution:

1. Initialize an empty deque and a list to store the rolling maximums.
2. Iterate through the numbers list. For each number:
    - If the deque is empty, append the number to the deque.
    - If the number is greater than the maximum number in the deque, append the number to the deque.
    - If the number is less than or equal to the maximum number in the deque, remove the minimum number from the deque and append the number.
3. Append the maximum number in the deque to the rolling maximums list.
4. Return the rolling maximums list.

Here's the code for the solution:

```python
from collections import deque

def rollingMax(numbers):
    # Initialize an empty deque and a list to store the rolling maximums
    deque_max = deque()
    rolling_max = []

    # Iterate through the numbers list
    for num in numbers:
        # If the deque is empty, append the number to the deque
        if not deque_max:
            deque_max.append(num)
        # If the number is greater than the maximum number in the deque, append the number to the deque
        elif num > deque_max[0]:
            deque_max.appendleft(num)
        # If the number is less than or equal to the maximum number in the deque, remove the minimum number from the deque and append the number
        else:
            deque_max.popleft()
            deque_max.append(num)
        # Append the maximum number in the deque to the rolling maximums list
        rolling_max.append(deque_max[0])

    return rolling_max
```

You can use the function like this:

```python
print(rollingMax