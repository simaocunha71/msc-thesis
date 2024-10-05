```
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
```


This function iterates over the given list of numbers, keeping track of the maximum value seen so far. It pushes this maximum value to the result list at each iteration. This way, the result list contains the rolling maximum element found until that moment in the sequence.

The time complexity of this function is O(n), where n is the number of elements in the input list, since it iterates over the list once. The space complexity is also O(n), as it creates a new list of the same length as the input list.