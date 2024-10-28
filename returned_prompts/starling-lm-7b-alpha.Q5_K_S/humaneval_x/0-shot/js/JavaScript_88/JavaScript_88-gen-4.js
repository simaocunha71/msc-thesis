Here's a simple approach to solve this problem:

1. If the sum of the first and last elements is odd, we need to sort the array in ascending order.
2. If the sum is even, we need to sort the array in descending order.
3. To achieve this, we can use the Array.sort() method, which sorts the array in place and returns the sorted array. The default sort order is built upon converting the elements into strings, comparing their sequences of UTF-16 code unit values and determining their relative order. However, we can pass a compare function to the Array.sort() method to customize the sort order.
4. We can define the compare function as follows:

  - If the sum of the first and last elements is odd, we can use the greater than (>) operator to compare the elements and return 1 to sort the array in ascending order.
  - If the sum is even, we can use the less than (<) operator to compare the elements and return -1 to sort the array in descending order.

5. Here's the implementation:

```javascript
const sortArray = (array) => {
  let sum = array[0] + array[array.length - 1];
  let sortOrder = sum % 2 === 0 ? -1 : 1;

  return array.sort((a, b) => sortOrder * (a - b));
};
```

This implementation first calculates the sum of the first and last elements of the array. If the sum is even, it sets the sortOrder variable to -1, indicating that the array should be sorted in descending order. If the sum is odd, it sets the sortOrder variable to 1, indicating that the array should be sorted in ascending order. Then, it uses the Array.sort() method with a compare function to sort the array based on the sortOrder variable.

The time complexity of this implementation is O(n log n), where n is the length of the input array.

Note: It's important to mention that this implementation modifies the original array. If you don't want to modify the original array, you can create a copy of the array and sort the copied array instead. Here's an example:

```javascript
const sortArray = (array) =>