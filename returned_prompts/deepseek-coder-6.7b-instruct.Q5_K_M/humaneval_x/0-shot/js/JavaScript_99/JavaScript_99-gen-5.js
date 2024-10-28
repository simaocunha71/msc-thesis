  const parsedValue = Number(value);
  const roundedValue = Math.round(parsedValue);

  if (roundedValue < parsedValue) {
    return parsedValue > 0 ? roundedValue + 1 : roundedValue - 1;
  }

  return roundedValue;
};

module.exports = closestInteger;
```

In the above code, we first convert the string to a number using `Number()`. Then we use `Math.round()` to round the number. If the rounded number is less than the original number, we return the rounded number plus or minus 1, depending on whether the original number is positive or negative. Otherwise, we return the rounded number.

This solution assumes that the input string will always represent a valid number. If the input string might not represent a valid number, you should add some error checking code to handle that case.

Here's the solution in JavaScript:

```javascript
const closestInteger = (value) => {
  const parsedValue = Number(value);
  const roundedValue = Math.round(parsedValue);

  if (roundedValue < parsedValue) {
    return parsedValue > 0 ? roundedValue + 1 : roundedValue - 1;
  }

  return roundedValue;
};

module.exports = closestInteger;
```

And here's how you can test it:

```javascript
console.log(closestInteger("10")); // Expected output: 10
console.log(closestInteger("15.3")); // Expected output: 15
console.log(closestInteger("14.5")); // Expected output: 15
console.log(closestInteger("-14.5")); // Expected output: -15
```

This solution is written in JavaScript. If you want a solution in a different language, you'll need to translate it.

Please let me know if you need help with anything else.





































































