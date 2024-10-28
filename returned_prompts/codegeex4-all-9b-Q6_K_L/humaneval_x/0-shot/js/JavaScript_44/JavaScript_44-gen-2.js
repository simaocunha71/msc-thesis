To change the numerical base of an input number `x` to a given base, you can repeatedly divide the number by the base and record the remainders. The remainders, read in reverse order, give the number in the new base. Here's how you can implement the `changeBase` function:

```javascript
const changeBase = (x, base) => {
  let result = '';
  while (x > 0) {
    // Calculate the remainder of x divided by the base
    const remainder = x % base;
    // Convert the remainder to a string and add it to the result
    result = remainder.toString() + result;
    // Update x by dividing it by the base
    x = Math.floor(x / base);
  }
  return result;
};
```

This function works as follows:

1. It initializes an empty string `result` to store the digits of the number in the new base.
2. It enters a loop that continues as long as `x` is greater than 0.
3. Inside the loop, it calculates the remainder when `x` is divided by the base. This is the next digit in the base representation of `x`.
4. It converts the remainder to a string and adds it to the front of the `result` string. This is done by prepending the remainder to `result`.
5. It updates `x` by dividing it by the base and using `Math.floor` to ensure it's an integer.
6. When `x` is 0, the loop ends, and the function returns the `result` string.

Here are some examples of how the function works:

```javascript
console.log(changeBase(8, 3)); // '22'
console.log(changeBase(8, 2)); // '1000'
console.log(changeBase(7, 2)); // '111'
```

In the first example, the number 8 is represented in base 3 as 22. In the second example, the number 8 is represented in base 2 as 1000. In the third example, the number 7 is represented in base 2 as 111.