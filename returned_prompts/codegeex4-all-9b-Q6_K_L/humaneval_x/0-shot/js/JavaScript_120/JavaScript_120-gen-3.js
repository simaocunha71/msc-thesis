```js
const maximum = (arr, k) => {
  if (k === 0) return [];
  let max = Math.max(...arr);
  let maxIndex = arr.indexOf(max);
  let result = arr.splice(maxIndex, 1);
  while (k > 1) {
    max = Math.max(...arr);
    maxIndex = arr.indexOf(max);
    result.push(arr.splice(maxIndex, 1)[0]);
    k -= 1;
  }
  return result.sort((a, b) => a - b);
};
```

Explanation:
1. Check if k is 0, if yes return an empty array.
2. Find the maximum value in the array.
3. Find the index of the maximum value in the array.
4. Remove the maximum value from the array and add it to the result array.
5. Repeat steps 2-4 k-1 times.
6. Sort the result array in ascending order and return it.