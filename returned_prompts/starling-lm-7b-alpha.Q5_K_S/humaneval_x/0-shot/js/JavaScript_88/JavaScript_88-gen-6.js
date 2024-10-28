The main goal of the task is to sort the array in ascending order if the sum of the first and last elements is odd, and in descending order if it is even.

To solve the problem, we can follow these steps:

1. Calculate the sum of the first and last elements of the array.
2. If the sum is odd, sort the array in ascending order. If the sum is even, sort the array in descending order.
3. Create a copy of the original array to avoid modifying the given array.
4. Use the sort() function to sort the copied array in the desired order.
5. Return the sorted array.

Here's the implementation of the solution:

```javascript
const sortArray = (array) => {
  const sum = array[0] + array[array.length - 1];

  const sortedArray = array.slice();

  if (sum % 2 === 0) {
    sortedArray.sort((a, b) => b - a);
  } else {
    sortedArray.sort((a, b) => a - b);
  }

  return sortedArray;
};
```

In this solution, we first calculate the sum of the first and last elements of the array. Then, we create a copy of the original array using the slice() method to avoid modifying the given array. After that, we sort the copied array in ascending order if the sum is odd, or in descending order if the sum is even. Finally, we return the sorted array.

You can test the function with the provided examples to verify its correctness:

```javascript
console.log(sortArray([])); // []
console.log(sortArray([5])); // [5]
console.log(sortArray([2, 4, 3, 0, 1, 5])); // [0, 1, 2, 3, 4, 5]
console.log(sortArray([2, 4, 3, 0, 1, 5, 6])); // [6, 5, 4, 3, 2, 1, 0]
```

The output of these tests should match the expected results.

Note:

1. In