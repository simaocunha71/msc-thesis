  return number - Math.floor(number);
};

console.log(truncateNumber(3.5)); // 0.5
console.log(truncateNumber(1.23)); // 0.23
console.log(truncateNumber(0.99)); // 0.99
console.log(truncateNumber(1.0)); // 0
```

The function takes a floating point number as an argument, subtracts the integer part of the number (using `Math.floor(number)`) from the original number, and returns the result, which is the decimal part of the original number.

```javascript
