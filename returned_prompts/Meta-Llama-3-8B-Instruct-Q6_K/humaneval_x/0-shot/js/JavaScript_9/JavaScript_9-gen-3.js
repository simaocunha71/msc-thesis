```
const rollingMax = (numbers) => {
  const result = [];
  let maxSoFar = numbers[0];

  for (let i = 1; i < numbers.length; i++) {
    const currentMax = Math.max(maxSoFar, numbers[i]);
    result.push(currentMax);
    maxSoFar = currentMax;
  }

  return result;
};
```


Explanation:
The problem is asking to create a function that generates a list of rolling maximum elements found until a given moment in a sequence of integers. The rolling maximum is the maximum value found in the sequence up to that point.

Here is the solution:

We create a new list `result` to store the rolling maximum elements. We also initialize a variable `maxSoFar` to store the maximum value found so far, which is set to the first element of the input list `numbers`.

We then iterate over the input list starting from the second element (index 1). For each element, we calculate the maximum between the current maximum `maxSoFar` and the current element `numbers[i]`. We then push this maximum value to the `result` list and update `maxSoFar` with the new maximum value.

Finally, we return the `result` list, which contains the rolling maximum elements for each moment in the sequence.

The time complexity of this solution is O(n), where n is the length of the input list, because we iterate over the list once. The space complexity is also O(n), because we create a new list to store the result.