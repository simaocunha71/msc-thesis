```javascript
const sortThird = (l) => {
  return l.map((value, index) => {
    if (index % 3 === 0) {
      return [...l.slice(index)].sort((a, b) => a - b)[0];
    } else {
      return value;
    }
  });
};
```
This function uses the `map` method to create a new array where each element is either the original value at that index or the smallest value at that index and its subsequent indices, if the index is divisible by 3. The smallest value at that index and its subsequent indices is obtained by slicing the original array from that index, sorting the slice in ascending order, and taking the first element of the sorted slice. The rest of the elements in the original array remain unchanged. The resulting array is returned as the output of the function.