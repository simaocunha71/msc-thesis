Here is a solution using JavaScript:
```
const sortArray = (arr) => {
  return arr.sort((a, b) => {
    if (a.toString(2).split('1').length - 1 === b.toString(2).split('1').length - 1) {
      return a - b;
    }
    return a.toString(2).split('1').length - 1 - b.toString(2).split('1').length + 1;
  });
};
```
Explanation:

* We use the `sort()` method to sort the array.
* Inside the callback function, we convert each number to a binary string using the `toString(2)` method.
* We split the binary string into an array of substrings using the `split('1')` method, which splits the string at each occurrence of the character '1'.
* We get the length of the resulting array minus 1, which gives us the number of ones in the binary representation of the number.
* If the number of ones is the same for both numbers, we compare the decimal values using the `a - b` expression.
* Otherwise, we return the difference in the number of ones, with a negative sign if the first number has fewer ones.

This solution works for both positive and negative integers, and it also handles the case where the input array is empty.