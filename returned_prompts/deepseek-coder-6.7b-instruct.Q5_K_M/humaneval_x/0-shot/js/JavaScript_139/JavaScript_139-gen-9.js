  let result = 1;
  for (let i = n; i > 0; i--) {
    result *= factorial(i);
  }
  return result;
};

const factorial = (n) => {
  let result = 1;
  for (let i = n; i > 0; i--) {
    result *= i;
  }
  return result;
};

console.log(specialFactorial(4)); // 288

//Explanation:
//The specialFactorial function calculates the brazilian factorial of n
//which is the product of factorials from n down to 1.
//The factorial function calculates the factorial of a given number.
```

## Testing

```javascript
console.log(specialFactorial(1)); // 1
console.log(specialFactorial(2)); // 2
console.log(specialFactorial(3)); // 12
console.log(specialFactorial(4)); // 288
console.log(specialFactorial(5)); // 34560
```

## Resources

- [Factorial (mathematics)](https://en.wikipedia.org/wiki/Factorial)
- [Brazilian factorial (mathematics)](https://en.wikipedia.org/wiki/Brazilian_factorial)
- [Javascript Loops](https://www.w3schools.com/js/js_loop_for.asp)
- [Javascript Function](https://www.w3schools.com/js/js_functions.asp)
- [Javascript Recursion](https://www.w3schools.com/js/js_recursion.asp)
- [Javascript Arrow Function](https://www.w3schools.com/js/js_arrow_functions.asp)
- [Javascript BigInt](https://www.w3schools.com/js/js_bigint.asp)
- [Javascript Operator Precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Preced