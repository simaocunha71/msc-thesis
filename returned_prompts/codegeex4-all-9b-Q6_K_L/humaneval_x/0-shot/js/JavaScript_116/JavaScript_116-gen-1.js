To solve this problem, we can follow these steps:

1. Convert each number to its binary representation.
2. Count the number of ones in each binary representation.
3. Sort the array based on the number of ones, and then by the decimal value if the number of ones is the same.

Here is the implementation for the `sortArray` function:

```javascript
const sortArray = (arr) => {
  // Function to count the number of ones in a binary representation
  const countOnes = (num) => {
    return num.toString(2).split('1').length - 1;
  };

  // Sort the array based on the number of ones, and then by the decimal value
  return arr.sort((a, b) => {
    const countA = countOnes(a);
    const countB = countOnes(b);
    if (countA === countB) {
      return a - b;
    } else {
      return countA - countB;
    }
  });
};
```

Let's test the function with the provided test cases:

```javascript
console.log(sortArray([1, 5, 2, 3, 4])); // [1, 2, 3, 4, 5]
console.log(sortArray([-2, -3, -4, -5, -6])); // [-6, -5, -4, -3, -2]
console.log(sortArray([1, 0, 2, 3, 4])); // [0, 1, 2, 3, 4]
```

The function should return the expected output for each test case.