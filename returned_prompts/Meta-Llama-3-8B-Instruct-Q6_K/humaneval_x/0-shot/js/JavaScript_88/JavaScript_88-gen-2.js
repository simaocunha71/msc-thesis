```
const sortArray = (array) => {
  const sum = array[0] + array[array.length - 1];
  const isOdd = sum % 2 !== 0;
  return isOdd ? array.slice().sort((a, b) => a - b) : array.slice().sort((a, b) => b - a);
};
```


Explanation:
The function takes an array as input and calculates the sum of the first and last elements. It then checks if the sum is odd or even. If the sum is odd, the array is sorted in ascending order. If the sum is even, the array is sorted in descending order.

The `slice()` method is used to create a copy of the original array, as per the problem statement. The `sort()` method is used to sort the array in either ascending or descending order, depending on the value of `isOdd`. The sorted array is then returned as the result.