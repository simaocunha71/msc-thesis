```
const sortArray = (array) => {
  const sum = array[0] + array[array.length - 1];
  return sum % 2 === 0
    ? array.slice().sort((a, b) => b - a)
    : array.slice().sort((a, b) => a - b);
};
```


Explanation:
The function `sortArray` takes an array as an argument and returns a new sorted array.
It calculates the sum of the first and last elements of the array, and then checks if the sum is even or odd.

If the sum is even, the function returns a new sorted array in descending order. If the sum is odd, the function returns a new sorted array in ascending order.

The `slice()` method is used to create a shallow copy of the original array, so the original array is not modified.

The `sort()` method is used to sort the array, and the compare function `(a, b) => b - a` is used to sort in descending order, and `(a, b) => a - b` is used to sort in ascending order.