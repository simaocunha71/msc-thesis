```javascript
const rollingMax = (numbers) => {
  return numbers.reduce((acc, current, index) => {
    if (index === 0) {
      return [current];
    }
    return [...acc, Math.max(...[...acc.slice(-1)][0], current)];
  }, []);
};
```

Explanation:
This function takes an array of numbers as input and returns an array of rolling maximum elements. The function uses the `reduce` method to iterate over the input array. For each element in the array, it calculates the maximum of the previous rolling maximum and the current element. The result is an array where each element is the maximum of the rolling maximum until that point in the sequence.

For example, for the input `[1, 2, 3, 2, 3, 4, 2]`, the function returns `[1, 2, 3, 3, 3, 4, 4]`. This means that the maximum element until the first element is 1, until the second element is 2, until the third element is 3, and so on.