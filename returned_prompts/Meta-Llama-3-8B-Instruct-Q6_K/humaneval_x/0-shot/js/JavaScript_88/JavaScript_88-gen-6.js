```javascript
const sortArray = (array) => {
  if (array.length === 0) {
    return array;
  }
  const sum = array[0] + array[array.length - 1];
  const isOdd = sum % 2 !== 0;
  return isOdd ? array.slice().sort((a, b) => a - b) : array.slice().sort((a, b) => b - a);
};
```
Explanation:
The function takes an array as an input and returns a new array which is a copy of the given array after sorting. The sorting order is determined by the sum of the first and last elements of the array. If the sum is odd, the array is sorted in ascending order; if the sum is even, the array is sorted in descending order.

The function uses the slice() method to create a copy of the original array, and the sort() method to sort the array. The sort() method takes a compare function as an argument, which is used to determine the sort order. The compare function takes two arguments, a and b, and returns a negative value if a is less than b, a positive value if a is greater than b, and 0 if a is equal to b.

In the code, the sum of the first and last elements of the array is calculated using the expression array[0] + array[array.length - 1]. The result is stored in the variable sum.

Then, the isOdd variable is set to true if the sum is odd, and false if the sum is even. This variable determines the sorting order.

Finally, the sorted array is returned using the return statement. If isOdd is true, the array is sorted in ascending order using the sort() method with a compare function that returns a - b. If isOdd is false, the array is sorted in descending order using the sort() method with a compare function that returns b - a.