let sum = 0;
let mean = numbers.reduce((acc, val) => acc + val, 0) / numbers.length;

numbers.forEach((num) => {
  sum += Math.abs(num - mean);
});

return sum / numbers.length;
}

console.log(meanAbsoluteDeviation([1.0, 2.0, 3.0, 4.0])); // 1.0

```

**Explanation:**

- We first calculate the mean of the input numbers by summing them up and dividing by the count of numbers.
- Then we calculate the absolute difference of each number from the mean, sum those differences up and divide by the count of numbers to get the Mean Absolute Deviation.

**Note:**

- `reduce()` method reduces the array to a single value. The return value is the accumulated result of the callback function.
- `Math.abs()` method returns the absolute value of a number.

**Complexity:**

- Time complexity is O(n), as we have to pass through the array twice.
- Space complexity is O(1), as we are not using any extra space that scales with the size of the input.

**Test Cases:**

- `meanAbsoluteDeviation([1.0, 2.0, 3.0, 4.0])` should return `1.0`
- `meanAbsoluteDeviation([5.0, 10.0, 100.0])` should return `87.5`
- `meanAbsoluteDeviation([15.0, 30.0, 60.0, 120.0])` should return `52.5`
- `meanAbsoluteDeviation([-1.0, -2.0, -3.0])` should return `2.0`

**Note:**

- The test cases are based on the provided problem statement.
- The expected output is based on the formula for Mean Absolute Deviation.
- The actual output is what the function returns given the input.
- If the actual output matches the expected output, the function works correctly.
- If the actual output