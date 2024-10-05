```javascript
const truncateNumber = (number) => {
  return number - Math.floor(number);
};

// Test cases
console.log(truncateNumber(3.5)); // Output: 0.5
console.log(truncateNumber(2.9)); // Output: 0.9
console.log(truncateNumber(5.0)); // Output: 0
```

Explanation:
The function `truncateNumber` takes a positive floating-point number as input and returns its decimal part. To achieve this, we can subtract the integer part (obtained using `Math.floor`) from the original number.

In the example above, we test the function with three different input values: `3.5`, `2.9`, and `5.0`. The output for each test case is the decimal part of the input number, as expected. For instance, the decimal part of `3.5` is `0.5`, which is correctly returned by the function. Similarly, the decimal parts of `2.9` and `5.0` are `0.9` and `0`, respectively, which are also correctly returned.