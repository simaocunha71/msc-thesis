To solve this problem, we can follow these steps:

1. Calculate the sum of the first and last elements of the array.
2. Check if the sum is odd or even. If it's odd, sort the array in ascending order. If it's even, sort the array in descending order.
3. Return the sorted array.

Here's the updated code:

```javascript
const sortArray = (array) => {
  const sum = array[0] + array[array.length - 1];
  if (sum % 2 === 1) {
    return array.slice().sort((a, b) => a - b);
  } else {
    return array.slice().sort((a, b) => b - a);
  }
};
```

We use the `slice()` method to create a copy of the array, so that we don't modify the original array. Then, we use the `sort()` method to sort the array in ascending order or descending order based on the sum.