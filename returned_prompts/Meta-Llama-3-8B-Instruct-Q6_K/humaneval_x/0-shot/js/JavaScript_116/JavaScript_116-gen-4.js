```
const sortArray = (arr) => {
  return arr.sort((a, b) => {
    const countA = (a.toString(2)).replace(/0/g, '').length;
    const countB = (b.toString(2)).replace(/0/g, '').length;
    if (countA === countB) {
      return a - b;
    }
    return countA - countB;
  });
};
```


This function works by first converting each number in the array to a binary string. It then counts the number of ones in each binary string, and uses these counts to determine the order of the numbers. If two numbers have the same number of ones, it sorts them based on their decimal values.

The `sort()` method is used to sort the array, and it takes a callback function as an argument. This callback function is called for each pair of adjacent elements in the array, and it should return a negative value if the first element should come before the second, a positive value if the second element should come before the first, and zero if the elements are equal.

In this case, the callback function checks the number of ones in the binary representation of each number, and returns the difference between these counts. If the counts are equal, it returns the difference between the decimal values of the numbers. This ensures that the array is sorted first by the number of ones, and then by the decimal value.