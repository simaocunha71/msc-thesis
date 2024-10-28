The task is to find the sum of all the elements in the first k elements of the array that have at most two digits.

Here is a simple and efficient solution in JavaScript:

```javascript
const addElements = (arr, k) => {
  let sum = 0;
  for (let i = 0; i < k; i++) {
    const num = arr[i];
    if (String(num).length <= 2) {
      sum += num;
    }
  }
  return sum;
};
```

This function iterates over the first k elements of the array. For each element, it checks if the length of the string representation of the element is less than or equal to 2 (which means the element has at most two digits). If the condition is true, it adds the element to the sum. Finally, it returns the sum.

For example, if we call `addElements([111,21,3,4000,5,6,7,8,9], 4)`, it will return `24` which is the sum of `21` and `3`.