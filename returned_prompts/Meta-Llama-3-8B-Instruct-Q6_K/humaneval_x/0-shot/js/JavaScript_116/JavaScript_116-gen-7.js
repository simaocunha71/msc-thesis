```
const sortArray = (arr) => {
  return arr.sort((a, b) => {
    const countA = a.toString(2).replace(/0+/g, '').length;
    const countB = b.toString(2).replace(/0+/g, '').length;
    if (countA === countB) {
      return a - b;
    }
    return countA - countB;
  });
};
```
Explanation:
The function `sortArray` takes an array of integers as input and returns a new sorted array. It uses the `sort` method to sort the array, and provides a compare function that determines the sort order.

In the compare function, we first convert each integer to its binary representation using the `toString(2)` method. We then use a regular expression to replace one or more consecutive zeros with an empty string, effectively counting the number of ones in the binary representation. We store these counts in `countA` and `countB`.

If the counts are equal, we sort based on the decimal value of the integers using the `-` operator.

If the counts are not equal, we sort based on the count of ones in ascending order.

The `sort` method returns a new sorted array, which is then returned by the `sortArray` function.