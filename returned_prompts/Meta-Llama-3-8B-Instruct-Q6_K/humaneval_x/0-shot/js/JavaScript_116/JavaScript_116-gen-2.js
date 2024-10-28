```
const sortArray = (arr) => {
  return arr.sort((a, b) => {
    let countA = (a.toString(2)).replace(/0/g, '').length;
    let countB = (b.toString(2)).replace(/0/g, '').length;
    if (countA === countB) {
      return a - b;
    }
    return countA - countB;
  });
};
```


Explanation:
The provided solution uses the built-in `sort()` method of JavaScript arrays. It takes a callback function as an argument, which is used to determine the sort order of the array.

 Inside the callback function, we calculate the number of ones in the binary representation of each number `a` and `b` using the `toString(2)` method, which converts the number to a binary string, and then the `replace(/0/g, '').length` method, which counts the number of ones by replacing all zeros with an empty string and getting the length of the resulting string.

If the number of ones is the same for both numbers, we compare them based on their decimal value using `a - b`. If the number of ones is different, we compare them based on the number of ones.

Finally, the `sort()` method returns a new sorted array. The `sortArray()` function returns this sorted array.