```
const sortArray = (arr) => {
  return arr.sort((a, b) => {
    if (a.toString(2).replace(/0/g, '').length !== b.toString(2).replace(/0/g, '').length) {
      return a.toString(2).replace(/0/g, '').length - b.toString(2).replace(/0/g, '').length;
    } else {
      return a - b;
    }
  });
};
```


This function uses the built-in `sort` method of JavaScript arrays. The callback function passed to `sort` is used to determine the sort order.

The callback function compares two elements `a` and `b` by first counting the number of ones in their binary representation. If the number of ones is different, it returns the difference.

If the number of ones is the same, it compares the decimal values of `a` and `b` and returns their difference.

This ensures that the array is sorted according to the number of ones in their binary representation in ascending order, and for similar numbers of ones, the decimal value is used for sorting.