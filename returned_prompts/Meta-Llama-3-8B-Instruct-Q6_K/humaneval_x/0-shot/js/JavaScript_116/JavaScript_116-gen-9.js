```
const sortArray = (arr) => {
  return arr.sort((a, b) => {
    if (a.toString(2).split('1').length - b.toString(2).split('1').length !== 0) {
      return a.toString(2).split('1').length - b.toString(2).split('1').length;
    } else {
      return a - b;
    }
  });
};
```


Explanation:
The task is to sort an array of non-negative integers based on the number of ones in their binary representation in ascending order. For similar numbers of ones, sort based on decimal value.

The solution uses the built-in JavaScript `sort` function, which sorts the array in-place. The comparison function is defined using an arrow function that takes two arguments, `a` and `b`.

 Inside the comparison function, we first check if the number of ones in the binary representation of `a` is different from the number of ones in the binary representation of `b`. If they are different, we return the difference. If they are the same, we return the difference between `a` and `b`.

The `toString(2)` method is used to convert the integers to binary strings, and the `split('1')` method is used to count the number of ones in the binary representation.

The comparison function is used by the `sort` function to determine the order of the elements in the array. The `sort` function then rearranges the elements in the array based on the comparison function. The resulting array is then returned by the `sortArray` function.