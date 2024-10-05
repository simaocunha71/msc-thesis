
Here's a simple solution to solve this problem:

1. First, we check the sum of the first and last elements of the array. If the sum is even, we sort the array in descending order, otherwise, we sort it in ascending order.
2. Then, we sort the array using the built-in sort method. We pass a compare function to the sort method, which compares two elements at a time and returns a value less than, equal to, or greater than zero. If the sum of the first and last elements is even, we return -1 to sort the array in descending order, otherwise, we return 1 to sort the array in ascending order.
3. Finally, we return the sorted array.

Here's the code to solve this problem:

```javascript
const sortArray = (array) => {
  const sum = array[0] + array[array.length - 1];
  const isEven = sum % 2 === 0;

  return array.sort((a, b) => isEven ? b - a : a - b);
};
```

This implementation has a time complexity of O(n log n), where n is the length of the array.

Note: This solution modifies the original array and returns a new sorted array. If you want to keep the original array unchanged, you can use the spread operator to create a copy of the array before sorting:

```javascript
const sortArray = (array) => {
  const sortedArray = [...array];
  const sum = sortedArray[0] + sortedArray[sortedArray.length - 1];
  const isEven = sum % 2 === 0;

  return sortedArray.sort((a, b) => isEven ? b - a : a - b);
};
```

This implementation has a time complexity of O(n log n) and a space complexity of O(n).

*/


const sortArray = (array) => {
  const sortedArray = [...array];
  const sum = sortedArray[0] + sortedArray[sortedArray.length - 1];
  const isEven = sum % 2 === 0;

  return sortedArray.sort((a, b) => isEven ? b -