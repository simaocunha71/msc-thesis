Here is a Python solution using list comprehension and the built-in functions `mean` and `abs` from the `statistics` module:

```python
import statistics

def meanAbsoluteDeviation(numbers):
    mean = statistics.mean(numbers)
    return statistics.mean([abs(x - mean) for x in numbers])
```

Here is a JavaScript solution using the `reduce` method and `Math.abs` function:

```javascript
function meanAbsoluteDeviation(numbers) {
    const mean = numbers.reduce((acc, current) => acc + current, 0) / numbers.length;
    return numbers.reduce((acc, current) => acc + Math.abs(current - mean), 0) / numbers.length;
}
```

Both solutions calculate the mean of the input list and then the mean absolute deviation by summing the absolute differences between each element and the mean, and dividing by the length of the list. The `statistics` module in Python provides the `mean` and `abs` functions, while in JavaScript, the `reduce` method is used to sum the elements. The `Math.abs` function is used to calculate the absolute differences. The results are then divided by the length of the list to get the mean absolute deviation. 

You can test these functions with the following code:

```python
print(meanAbsoluteDeviation([1.0, 2.0, 3.0, 4.0]))  # Output: 1.0
```

```javascript
console.log(meanAbsoluteDeviation([1.0, 2.0, 3.0, 4.0]));  // Output: 1.0
```  