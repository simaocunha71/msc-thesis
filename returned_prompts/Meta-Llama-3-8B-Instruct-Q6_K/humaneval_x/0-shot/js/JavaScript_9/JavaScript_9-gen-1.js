```javascript
const rollingMax = (numbers) => {
  let maxSoFar = numbers[0];
  let result = [numbers[0]];
  for(let i = 1; i < numbers.length; i++) {
    if(numbers[i] > maxSoFar) {
      maxSoFar = numbers[i];
    }
    result.push(maxSoFar);
  }
  return result;
};
```


Explanation:

1. Initialize `maxSoFar` with the first element of the `numbers` array, and `result` with a single element, which is the first element of the `numbers` array.
2. Iterate through the `numbers` array starting from the second element (index 1).
3. For each element, check if it is greater than `maxSoFar`. If it is, update `maxSoFar` with the current element.
4. Push `maxSoFar` into the `result` array.
5. Return the `result` array, which contains the rolling maximum elements.

The output for the given example input `[1, 2, 3, 2, 3, 4, 2]` would be `[1, 2, 3, 3, 3, 4, 4]`. The rolling maximum elements are 1, 2, 3, 3, 3, 4, and 4, which are the maximum elements found up to each moment in the sequence.