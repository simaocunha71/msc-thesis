Here is a solution in JavaScript:

```javascript
const rollingMax = (numbers) => {
  let max = numbers[0];
  let results = [max];

  for (let i = 1; i < numbers.length; i++) {
    if (numbers[i] > max) {
      max = numbers[i];
    }
    results.push(max);
  }

  return results;
};
```
This function starts by assuming the first number is the maximum. It then iterates over the rest of the numbers, updating the maximum if it finds a larger number. It also adds the current maximum to the results array on each iteration. The function then returns the results array, which contains the rolling maximum values.