Here is the solution in JavaScript:
```
const generateIntegers = (a, b) => {
  let result = [];
  for (let i = Math.min(a, b); i <= Math.max(a, b); i++) {
    const str = i.toString();
    for (let j = 0; j < str.length; j++) {
      if (str[j] % 2 === 0) {
        result.push(parseInt(str[j]));
      }
    }
  }
  return result.filter((x, i) => result.indexOf(x) === i);
};
```
Here's an explanation of the code:

1. We first find the minimum and maximum values of `a` and `b` using `Math.min` and `Math.max`.
2. We then loop through each integer between `a` and `b` using a `for` loop.
3. For each integer, we convert it to a string using `toString()`.
4. We then loop through each character in the string using another `for` loop.
5. For each character, we check if it's an even digit by checking if the remainder of the character's ASCII value divided by 2 is 0. If it is, we add the character to the `result` array.
6. Finally, we filter the `result` array to remove duplicates by using the `filter` method with a callback function that checks if the current element is equal to the first occurrence of that element in the array.

Note that this solution assumes that the input integers are positive. If you want to handle negative integers as well, you'll need to modify the solution accordingly. Also, this solution returns an array of even digits, not integers. If you want to return an array of integers, you can modify the solution to use `parseInt` instead of converting the character to an integer.