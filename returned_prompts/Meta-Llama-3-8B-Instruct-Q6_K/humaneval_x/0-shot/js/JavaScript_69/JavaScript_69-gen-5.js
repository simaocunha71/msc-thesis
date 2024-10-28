Here is the solution to the problem:
```
const search = (lst) => {
  const freqMap = {};
  for (const num of lst) {
    if (freqMap[num]) {
      freqMap[num]++;
    } else {
      freqMap[num] = 1;
    }
  }
  let maxNum = -1;
  for (const [num, freq] of Object.entries(freqMap)) {
    if (freq >= parseInt(num)) {
      maxNum = Math.max(maxNum, parseInt(num));
    }
  }
  return maxNum;
};
```
Here's an explanation of the solution:

1. First, we create an object `freqMap` to store the frequency of each number in the list.
2. We iterate through the list and update the frequency of each number in `freqMap`.
3. Then, we iterate through the `freqMap` object and find the maximum number that has a frequency greater than or equal to its value. We use `parseInt` to convert the number to an integer, since we're comparing with its frequency.
4. If no such number is found, we return -1.

Let's test the function with the examples provided:
```
console.log(search([4, 1, 2, 2, 3, 1])); // Output: 2
console.log(search([1, 2, 2, 3, 3, 3, 4, 4, 4])); // Output: 3
console.log(search([5, 5, 4, 4, 4])); // Output: -1
```
The function returns the expected results for each example.