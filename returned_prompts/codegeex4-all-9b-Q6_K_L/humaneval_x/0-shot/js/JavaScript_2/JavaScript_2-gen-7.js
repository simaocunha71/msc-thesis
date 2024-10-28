You can use the remainder operator (%) to get the decimal part of the number. The remainder operator returns the remainder left after a division operation. For example, 3.5 % 1 will give you 0.5.
Here is the solution:

```javascript
const truncateNumber = (number) => {
  return number % 1;
};
```

This function will return the decimal part of the number. For example, truncateNumber(3.5) will return 0.5.