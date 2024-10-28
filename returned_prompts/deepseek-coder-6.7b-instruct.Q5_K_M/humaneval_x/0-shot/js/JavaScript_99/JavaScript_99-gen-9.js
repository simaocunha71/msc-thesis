  let num = parseFloat(value);

  return (num < 0) ? Math.floor(num - 0.5) : Math.floor(num + 0.5);
}

console.log(closestInteger("10")) // 10
console.log(closestInteger("15.3")) // 15
console.log(closestInteger("14.5")) // 15
console.log(closestInteger("-14.5")) // -15

// The function works by parsing the string to a float, then using
// Math.floor() to round the number down to the nearest integer.
// If the number is less than zero, we subtract 0.5 before rounding,
// otherwise we add 0.5 before rounding. This results in numbers that
// are always rounded away from zero when they are equidistant from
// two integers.

// Note: The Math.floor() function rounds a number down to the nearest integer.
// So, for example, Math.floor(15.3) would result in 15, while Math.floor(14.5) would result in 14.
// Adding or subtracting 0.5 allows us to move the decimal point one place to the right,
// effectively rounding the number away from zero when it is equidistant from two integers.
// If the number is negative, we subtract 0.5, if it is positive we add 0.5.


// This function is now able to handle negative numbers as well, as per the problem's requirements.
```

## Answer 2
```javascript
