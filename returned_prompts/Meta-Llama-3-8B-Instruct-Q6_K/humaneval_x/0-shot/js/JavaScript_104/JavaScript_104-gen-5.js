Here is the solution to the problem:

```javascript
const uniqueDigits = (x) => {
  return x.filter(num => {
    const str = num.toString();
    return !str.includes('2') && !str.includes('4') && !str.includes('6') && !str.includes('8');
  }).sort((a, b) => a - b);
};
```
The function `uniqueDigits` takes a list of positive integers `x` as input. It filters out the numbers that have any even digits (2, 4, 6, or 8) and returns the remaining numbers in a sorted list. The `filter` method is used to iterate over the list and check for the presence of even digits. The `includes` method is used to check if a string (the number converted to a string) contains a specific character. The `sort` method is used to sort the remaining numbers in increasing order.

For example, if the input is `[15, 33, 1422, 1]`, the function will return `[1, 15, 33]`, and if the input is `[152, 323, 1422, 10]`, the function will return an empty list `[]`. This is because the numbers 152, 1422, and 10 have even digits. The number 323 does not have any even digits, so it is included in the output. The number 1 does not have any even digits, so it is also included in the output. The numbers 15 and 33 do not have any even digits, so they are also included in the output. The numbers 1422 and 10 have even digits, so they are not included in the output. Therefore, the output is `[1, 15, 33]`.