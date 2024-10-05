```
const uniqueDigits = (x) => {
  return x.filter(num => !num.toString().includes('2') && !num.toString().includes('4') && !num.toString().includes('6') && !num.toString().includes('8') && !num.toString().includes('0')).sort((a, b) => a - b);
}
```
Explanation:
The function `uniqueDigits` takes a list of positive integers `x` as input.
It filters out the numbers that have any even digit (0, 2, 4, 6, 8) using the `filter` method.
The filter condition is `!num.toString().includes('2') && !num.toString().includes('4') && !num.toString().includes('6') && !num.toString().includes('8') && !num.toString().includes('0')`, which checks if the string representation of the number contains any of the even digits.
The remaining numbers are then sorted in increasing order using the `sort` method and returned as the result.

For example, if the input is `[15, 33, 1422, 1]`, the function will filter out `1422` and return the sorted list `[1, 15, 33]`. If the input is `[152, 323, 1422, 10]`, the function will filter out all numbers except `323` and return the sorted list `[]`.