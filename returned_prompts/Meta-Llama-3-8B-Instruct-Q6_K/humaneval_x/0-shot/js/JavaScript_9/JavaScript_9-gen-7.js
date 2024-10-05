```
const rollingMax = (numbers) => {
  const result = [];
  let maxSoFar = numbers[0];
  result.push(maxSoFar);

  for (let i = 1; i < numbers.length; i++) {
    if (numbers[i] > maxSoFar) {
      maxSoFar = numbers[i];
    }
    result.push(maxSoFar);
  }

  return result;
};
```


This function iterates over the input list of numbers, keeping track of the maximum number seen so far. Each time it encounters a new maximum, it updates the `maxSoFar` variable and appends the new maximum to the result list. At the end of the iteration, the result list will contain the rolling maximum for each position in the input list. The function then returns this list.