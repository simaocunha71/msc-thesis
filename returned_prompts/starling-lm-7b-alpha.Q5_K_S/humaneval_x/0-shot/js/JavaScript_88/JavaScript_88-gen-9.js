One possible solution is:

```javascript
const sortArray = (array) => {
  const sorted = array.slice();
  const first = array[0];
  const last = array[array.length - 1];
  sorted.sort((a, b) => (first + last) % 2 ? a - b : b - a);
  return sorted;
};
```

Explanation:

The function `sortArray` takes an array as a parameter, creates a copy of the array using the `slice` method, and assigns the first and last values to `first` and `last`.

The `sort` method is then used on the `sorted` array. The `sort` method takes a comparison function as a parameter, which determines the sorting order. In this case, the comparison function checks if the sum of the first and last values is odd (`(first + last) % 2`). If the sum is odd, the comparison function returns `a - b`, which sorts the array in ascending order. If the sum is even, the comparison function returns `b - a`, which sorts the array in descending order.

Finally, the sorted array is returned as the result of the function.

This solution ensures that the original array is not modified and returns a new sorted array based on the sum of the first and last values.

Note: The `slice` method is used to create a copy of the array to avoid modifying the original array while sorting.

Overall, this solution provides a clear and concise way to sort the array based on the sum of the first and last values, with the option to sort in ascending or descending order depending on whether the sum is odd or even.

The time complexity of this solution is O(n log n), where n is the number of elements in the array, due to the use of the `sort` method. The space complexity is O(1) as a new array is created to store the sorted result, and no additional space is required beyond the input array.

The solution is straightforward and easy to understand, making it a good choice for solving the problem at hand.

It is important to note that this solution assumes that the input array is non-empty and contains only non-negative integers.

In terms of performance, this solution is