```
const maximum = (arr, k) => {
  // Sort the array in descending order
  arr.sort((a, b) => b - a);
  
  // Return the first k elements of the sorted array
  return arr.slice(0, k);
};
```

This solution works by first sorting the array in descending order using the `sort()` method. This ensures that the maximum k numbers are at the beginning of the array. Then, it returns the first k elements of the sorted array using the `slice()` method. This is a simple and efficient solution that has a time complexity of O(n log n) due to the sorting operation.