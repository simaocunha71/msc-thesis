Here is the solution for the problem:

```javascript
const rollingMax = (numbers) => {
  let maxSoFar = numbers[0];
  let result = [numbers[0]];
  
  for (let i = 1; i < numbers.length; i++) {
    if (numbers[i] > maxSoFar) {
      maxSoFar = numbers[i];
    }
    result.push(maxSoFar);
  }
  
  return result;
};

console.log(rollingMax([1, 2, 3, 2, 3, 4, 2])); // Output: [1, 2, 3, 3, 3, 4, 4]
```

The function `rollingMax` takes a list of integers as an input and returns a list of rolling maximum element found until given moment in the sequence. The function initializes the `maxSoFar` variable with the first element of the list and the `result` list with the first element of the list. Then, it iterates over the list starting from the second element. If the current element is greater than `maxSoFar`, it updates `maxSoFar` with the current element. It then pushes `maxSoFar` into the `result` list. Finally, it returns the `result` list. The function uses a simple iterative approach to solve the problem. The time complexity is O(n), where n is the length of the input list. The space complexity is also O(n), as it needs to store the result list.