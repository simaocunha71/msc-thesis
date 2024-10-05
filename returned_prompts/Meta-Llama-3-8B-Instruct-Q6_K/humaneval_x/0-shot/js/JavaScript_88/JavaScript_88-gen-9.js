```
const sortArray = (array) => {
  const sumFirstLast = array[0] + array[array.length - 1];
  const isOdd = sumFirstLast % 2 !== 0;
  if (isOdd) {
    return array.slice().sort((a, b) => a - b);
  } else {
    return array.slice().sort((a, b) => b - a);
  }
};
```


Explanation:
The function `sortArray` takes an array of non-negative integers as input and returns a copy of the given array after sorting. It first calculates the sum of the first and last elements of the array. If the sum is odd, it sorts the array in ascending order; otherwise, it sorts the array in descending order. 

To avoid modifying the original array, it uses the `slice()` method to create a copy of the array and then sorts the copy. The sorted copy is then returned. 

The `sort()` method is used to sort the array, and the `slice()` method is used to create a copy of the array. The `slice()` method returns a shallow copy of the array, which is a new array object that has the same elements as the original array. 

In the sorting logic, it uses the `sort()` method with a compare function to sort the array. The compare function takes two arguments `a` and `b` and returns a negative value if `a` should come before `b`, a positive value if `b` should come before `a`, and 0 if they are equal. 

For ascending order, the compare function returns `a - b` which is a negative value if `a` is smaller than `b`, a positive value if `b` is smaller than `a`, and 0 if they are equal. 

For descending order, the compare function returns `b - a` which is a negative value if `b` is smaller than `a`, a positive value if `a` is smaller than `b`, and 0 if they are equal. 

The `sort()` method sorts the array in-place, meaning that it modifies the original array. To avoid modifying the original array, it uses the `slice()` method to create a copy of the array and then sorts the copy. 

This approach ensures that the original array remains unchanged, and a new sorted array is returned. 

The time complexity of this approach is O(n log n) where n is the length of the input array,