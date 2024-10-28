```javascript
const truncateNumber = (number) => {
  return number - Math.floor(number);
};
```

Explanation:
The function `truncateNumber` takes a floating point number as an argument. It returns the decimal part of the number by subtracting the integer part from the original number.

In JavaScript, `Math.floor(number)` returns the largest integer smaller than or equal to the number. So, `number - Math.floor(number)` effectively gives the decimal part of the number. This is because the integer part is removed, leaving only the decimal part.

For example, if the input is `3.5`, `Math.floor(3.5)` returns `3`, so `3.5 - 3` equals `0.5`, which is the decimal part of the number. This is why the output is `0.5` in this case.