Here is a Python solution for the problem:
```
def meanAbsoluteDeviation(numbers):
    mean = sum(numbers) / len(numbers)
    return sum(abs(num - mean) for num in numbers) / len(numbers)
```
This function calculates the mean of the input list, then calculates the absolute difference between each number and the mean. It then returns the average of these absolute differences, which is the mean absolute deviation.

For example, if you call `meanAbsoluteDeviation([1.0, 2.0, 3.0, 4.0])`, it will return `1.0`.

Here is a JavaScript solution for the problem:
```
function meanAbsoluteDeviation(numbers) {
  let mean = numbers.reduce((a, b) => a + b, 0) / numbers.length;
  return numbers.reduce((a, b) => a + Math.abs(b - mean), 0) / numbers.length;
}
```
This function calculates the mean of the input array, then calculates the absolute difference between each number and the mean. It then returns the average of these absolute differences, which is the mean absolute deviation.

For example, if you call `meanAbsoluteDeviation([1.0, 2.0, 3.0, 4.0])`, it will return `1.0`.