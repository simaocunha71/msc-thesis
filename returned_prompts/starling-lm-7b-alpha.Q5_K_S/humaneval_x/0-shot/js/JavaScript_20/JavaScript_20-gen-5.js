To solve this problem we need to find the two closest elements from the given list. We can do this by first sorting the array and then comparing adjacent elements. Here's a step-by-step breakdown of the solution:

1. Sort the given array using the `sort()` method. This will arrange the elements in ascending order.
2. Initialize two variables, `closest` and `minDiff`, to store the closest elements and the minimum difference between them, respectively. Set `minDiff` to infinity initially.
3. Iterate through the sorted array using a `for...of` loop, starting from the first element.
4. For each element, compare it with the next element. Calculate the absolute difference between the two using `Math.abs()`.
5. If the calculated difference is less than the current `minDiff`, update `closest` to the current element and `minDiff` to the calculated difference.
6. Once the loop is complete, return the `closest` elements in the desired format, `(smaller_number, larger_number)`.

Here's the code that implements the solution:

```python
def findClosestElements(numbers):
    # Sort the given array
    numbers = sorted(numbers)
    
    # Initialize closest and minDiff
    closest = (numbers[0], numbers[1])
    minDiff = float('inf')
    
    # Compare adjacent elements and update closest and minDiff
    for i in range(len(numbers)-1):
        diff = abs(numbers[i+1] - numbers[i])
        if diff < minDiff:
            closest = (numbers[i], numbers[i+1])
            minDiff = diff
    
    return closest
```

You can use this function by passing in a list of numbers as an argument. It will return a tuple containing the two closest elements in ascending order.

For example, if you call `findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])`, it will return `(2.0, 2.2)` because these two numbers are the closest to each other in the given list.

Similarly, if you