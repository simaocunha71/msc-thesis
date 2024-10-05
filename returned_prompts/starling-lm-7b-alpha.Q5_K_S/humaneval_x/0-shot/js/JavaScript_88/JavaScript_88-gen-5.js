Here's one possible way to solve this problem:

1. First, we need to calculate the sum of the first and last element of the array. We can use the formula sum = array[0] + array[array.length - 1].
2. Next, we need to determine whether the sum is even or odd. We can use the modulo operator % to check if the sum is divisible by 2. If the sum % 2 is equal to 0, then the sum is even; otherwise, it is odd.
3. If the sum is even, we need to sort the array in descending order. We can use the array.sort() method and pass a comparison function that returns -1 if a is greater than b, 1 if a is less than b, or 0 if a and b are equal. In this case, the comparison function should be (a, b) => b - a.
4. If the sum is odd, we need to sort the array in ascending order. We can use the same array.sort() method and comparison function as in step 3, but change the order of the operands in the comparison function to a - b.
5. Finally, we can return the sorted array.

Here's the code that implements the above steps:

```javascript
const sortArray = (array) => {
  const sum = array[0] + array[array.length - 1];

  if (sum % 2 === 0) {
    array.sort((a, b) => b - a);
  } else {
    array.sort((a, b) => a - b);
  }

  return array;
};
```

This implementation will correctly sort the given array in ascending order if the sum of the first and last elements is odd, and in descending order if the sum is even.

Note: It's important to note that this implementation modifies the original array. If you want to keep the original array unchanged, you should make a copy of the array before sorting it.

Also, the array.sort() method in JavaScript sorts the array in place, which means that the original array is modified directly. If you need to preserve the original array, you can use the spread operator (...) to create a new array and sort that instead.