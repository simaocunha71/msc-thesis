The task is to create a function `generateIntegers` that takes two positive integers `a` and `b` as input and returns an array of even digits between `a` and `b` in ascending order.

Here's the solution:
```javascript
const generateIntegers = (a, b) => {
  let result = [];
  for (let i = Math.min(a, b); i <= Math.max(a, b); i++) {
    let str = i.toString();
    for (let j = 0; j < str.length; j++) {
      if (+str[j] % 2 === 0) {
        result.push(+str[j]);
      }
    }
  }
  return result.filter((x, i, a) => a.indexOf(x) === i).sort((a, b) => a - b);
};
```
Here's an explanation of the code:

1. We initialize an empty array `result` to store the even digits.
2. We use a `for` loop to iterate from the minimum of `a` and `b` to the maximum.
3. Inside the loop, we convert the current number to a string `str` and iterate over its characters using another `for` loop.
4. For each character, we check if it's an even digit by using the modulo operator (`%`). If it is, we convert it back to an integer using the `+` operator and push it to the `result` array.
5. After the loops, we use the `filter` method to remove duplicates from the `result` array by comparing each element with its index in the array.
6. Finally, we sort the `result` array in ascending order using the `sort` method.

You can test this function with different inputs, like `generateIntegers(2, 8)` or `generateIntegers(8, 2)`. It should return the expected output.