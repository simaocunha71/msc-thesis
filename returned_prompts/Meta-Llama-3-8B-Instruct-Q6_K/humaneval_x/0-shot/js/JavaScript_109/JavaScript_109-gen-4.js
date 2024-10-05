Here is a possible solution in JavaScript:

```javascript
const moveOneBall = (arr) => {
  if (arr.length === 0) {
    return true;
  }

  let minIndex = 0;
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < arr[minIndex]) {
      minIndex = i;
    }
  }

  let shifts = minIndex;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > arr[(i + shifts) % arr.length]) {
      return false;
    }
  }

  return true;
};
```

This solution works by first finding the minimum element in the array, which will be the first element in the sorted array. Then, it checks if shifting the array to the right by the minimum index will result in a non-decreasing order. If it does, the function returns true; otherwise, it returns false. If the array is empty, the function returns true because an empty array is considered sorted.

For example, for the input `[3, 4, 5, 1, 2]`, the function will first find the minimum element `1` at index `3`. Then, it will shift the array to the right by `3` positions to get the sorted array `[1, 2, 3, 4, 5]`, which is a non-decreasing order. Therefore, the function will return `true`. For the input `[3, 5, 4, 1, 2]`, the function will find the minimum element `1` at index `3` and shift the array to the right by `3` positions to get the array `[4, 1, 2, 3, 5]`, which is not a non-decreasing order. Therefore, the function will return `false`.