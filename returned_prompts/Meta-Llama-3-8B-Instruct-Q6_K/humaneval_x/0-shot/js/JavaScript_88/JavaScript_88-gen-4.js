```
const sortArray = (array) => {
  if (array.length === 0) return array;
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
Explanation:
The provided function `sortArray` takes an array of non-negative integers as input. It first checks if the array is empty. If it is, the function returns the original array.

Then, it calculates the sum of the first and last elements of the array using the variables `sum`.

Next, it creates a copy of the original array using the `slice` method, which returns a shallow copy of the array. This copy is stored in the variable `sortedArray`.

Finally, based on the value of `sum`, it sorts the `sortedArray`. If `sum` is even, it sorts the array in descending order using the `sort` method with a compare function that returns the difference between the two elements in descending order (`b - a`). If `sum` is odd, it sorts the array in ascending order using the `sort` method with a compare function that returns the difference between the two elements in ascending order (`a - b`).

The function then returns the sorted `sortedArray`. If the array is empty, the function returns the original array. If the array has only one element, the function returns the same array (since it is already sorted). Otherwise, the function returns a sorted array based on the sum of the first and last elements.