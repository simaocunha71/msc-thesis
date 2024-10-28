To solve this problem, we can use a nested for loop to check all possible combinations of three distinct elements in the list. We can then add up these three elements and check if the sum is equal to zero. Here's the step-by-step solution:

1. Define a function called triplesSumToZero that takes a list of integers called "l" as an input.
2. Use a nested for loop to iterate through all possible combinations of three distinct elements in the list. The outer loop iterates through the first element of the combination, while the inner loop iterates through the second element. The third element will be determined by the difference between the sum of the first two elements and zero.
3. Inside the inner loop, add up the first two elements of the combination and subtract the result from zero to get the third element. Check if the third element is present in the list using the includes() method. If it is not present, return false. If it is present, continue to the next iteration of the outer loop.
4. After the nested loops have finished iterating through all possible combinations, return true if no combination was found that sums to zero, and false otherwise.

This solution has a time complexity of O(n^3), where "n" is the length of the input list, as we need to check all possible combinations of three elements. The space complexity is O(1) as we are not using any additional data structures that scale with the input size.

Here's the implementation of the solution in JavaScript:

```javascript
const triplesSumToZero = (l) => {
  for (let i = 0; i < l.length - 2; i++) {
    for (let j = i + 1; j < l.length - 1; j++) {
      let k = l[i] + l[j] - 0;
      if (l.includes(k) && i !== j) {
        return true;
      }
    }
  }
  return false;
};
```

You can test the function with the provided test cases to verify its correctness:

```javascript
console.log(triplesSumToZero([1, 3, 5, 0])); // false
console.log(triplesSumToZero([1, 3