The following JavaScript code creates a new array by inserting a number 'delimeter' between every two consecutive elements of the input list `numbers`:

```javascript
const intersperse = (numbers, delimeter) => {
  if (numbers.length === 0) {
    return [];
  }
  return numbers.reduce((acc, curr, index) => {
    if (index === 0) {
      return [curr];
    } else {
      return acc.concat([delimeter, curr]);
    }
  }, []);
}
```

This function uses the `reduce` method to create a new array by concatenating the 'delimeter' and the current element of the `numbers` array to the accumulator array (`acc`). If the current element is the first element of the `numbers` array, it is returned as is. Otherwise, the 'delimeter' and the current element are concatenated to the accumulator array. The final result is an array where the 'delimeter' is inserted between every two consecutive elements of the input list `numbers`.