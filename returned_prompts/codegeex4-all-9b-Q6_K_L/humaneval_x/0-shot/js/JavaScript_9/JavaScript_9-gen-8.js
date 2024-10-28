```javascript
const rollingMax = (numbers) => {
  let max = numbers[0];
  let result = [max];
  for (let i = 1; i < numbers.length; i++) {
    if (numbers[i] > max) {
      max = numbers[i];
    }
    result.push(max);
  }
  return result;
}
```

This solution iterates over the given list of numbers and keeps track of the current maximum value seen so far. It then pushes this maximum value to the result list on each iteration. If a new number is greater than the current maximum, it updates the maximum and pushes the new maximum to the result list.