  return number - Math.floor(number);
};

console.log(truncateNumber(3.5)); // 0.5
```

This function works by subtracting the floor of the number from the original number. The floor of a number is the largest integer less than or equal to the number. So this essentially gives you the leftover part after subtracting the integer part of the number, giving you the decimal part.

This also makes use of JavaScript's built-in Math.floor() function, which rounds a number down to the nearest whole number.

```javascript
// For example, if we have the number 3.5,
// Math.floor(3.5) would be 3,
// and 3.5 - 3 would be 0.5,
// which is the decimal part of 3.5.
```

So, `truncateNumber(3.5)` would return `0.5`.



## 3. String to Number Conversion

