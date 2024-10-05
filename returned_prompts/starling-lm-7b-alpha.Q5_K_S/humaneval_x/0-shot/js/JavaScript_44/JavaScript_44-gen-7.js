To convert a number in one base to another, you can use the following steps:

1. Convert the input number x to a string. This can be done using the toString() method in JavaScript. For example, x.toString(10).
2. Split the string into an array of digits. This can be done using the split('') method in JavaScript. For example, Array.from(x.toString(10).split('')).
3. Convert each digit from the original base to the new base. This can be done using a function that takes the digit, the original base, and the new base as parameters. For example, digit => { return parseInt(digit, originalBase).toString(newBase); }.
4. Join the converted digits back into a string. This can be done using the join('') method in JavaScript. For example, Array.from(x.toString(10).split('')).map(digit => { return parseInt(digit, originalBase).toString(newBase); }).join('');
5. Return the resulting string representation of the number in the new base. For example, Array.from(x.toString(10).split('')).map(digit => { return parseInt(digit, originalBase).toString(newBase); }).join('');

Here is an example of how to use the changeBase function:

```javascript
console.log(changeBase(8, 3)); // '22'
console.log(changeBase(8, 2)); // '1000'
console.log(changeBase(7, 2)); // '111'
```

In the example above, the changeBase function is called with different input values for x and base. The function converts the number x to a string, splits the string into an array of digits, converts each digit from the original base to the new base, joins the converted digits back into a string, and returns the resulting string representation of the number in the new base.

The changeBase function is a useful tool for converting numbers from one base to another, especially when working with binary or hexadecimal representations.

Overall, the changeBase function is a simple and effective way to convert a number in one base to another, and it can be easily integrated into any programming project that requires number