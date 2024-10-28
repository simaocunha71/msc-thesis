```
const rollingMax = (numbers) => {
  const result = [];
  let maxSoFar = numbers[0];
  for (let i = 1; i < numbers.length; i++) {
    result.push(Math.max(maxSoFar, numbers[i]));
    maxSoFar = Math.max(maxSoFar, numbers[i]);
  }
  return result;
};

console.log(rollingMax([1, 2, 3, 2, 3, 4, 2])); // [1, 2, 3, 3, 3, 4, 4]
```


Explanation:
1. Initialize an empty list `result` to store the rolling maximum elements.
2. Initialize `maxSoFar` with the first element of the input list `numbers`.
3. Iterate through the input list `numbers` starting from the second element (index 1).
4. In each iteration, calculate the maximum between `maxSoFar` and the current element using `Math.max`.
5. Push the calculated maximum into the `result` list.
6. Update `maxSoFar` with the calculated maximum.
7. Return the `result` list.

This solution has a time complexity of O(n), where n is the length of the input list, as it iterates through the list once. The space complexity is O(n) as well, as it stores the rolling maximum elements in the `result` list.