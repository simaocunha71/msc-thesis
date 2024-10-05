```
const sortArray = (arr) => {
  return arr.sort((a, b) => {
    const onesA = a.toString(2).replace(/0/g, '').length;
    const onesB = b.toString(2).replace(/0/g, '').length;
    if (onesA === onesB) {
      return a - b;
    }
    return onesA - onesB;
  });
};
```



Explanation:
The problem is asking to sort an array of non-negative integers based on the number of ones in their binary representation in ascending order. If two numbers have the same number of ones, they should be sorted based on their decimal value in ascending order.

In the provided solution, the `sortArray` function uses the built-in `sort` method of the array to sort the elements. The comparison function passed to the `sort` method takes two elements `a` and `b` as arguments, and returns a value that determines their order in the sorted array.

The comparison function first calculates the number of ones in the binary representation of `a` and `b` using the `toString(2)` method to convert the numbers to binary strings, and then replacing all zeros with an empty string using the `replace(/0/g, '')` method. The `length` property of the resulting string gives the number of ones.

If the number of ones is the same for both `a` and `b`, the comparison function returns the difference between `a` and `b` as integers, which sorts them based on their decimal value.

If the number of ones is different, the comparison function returns the difference between the number of ones as an integer, which sorts them based on the number of ones in ascending order.

The `sort` method uses this comparison function to sort the array, and the resulting sorted array is returned by the `sortArray` function.