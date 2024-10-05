```
const addElements = (arr, k) => {
  let sum = 0;
  for (let i = 0; i < k; i++) {
    if (String(arr[i]).length <= 2) {
      sum += arr[i];
    }
  }
  return sum;
};
```

The function iterates over the first k elements of the array. For each element, it checks if the length of the element as a string is less than or equal to 2. If it is, it adds the element to the sum. Finally, it returns the sum.

For the given example, the output would be 24, which is the sum of 21 and 3.