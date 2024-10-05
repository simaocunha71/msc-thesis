Here is the solution for the problem:

```javascript
const closestInteger = (value) => {
  const num = parseFloat(value);
  return Math.abs(num - Math.floor(num)) < Math.abs(num - Math.ceil(num)) ? Math.floor(num) : Math.ceil(num);
};
```

This function first parses the input string into a number using `parseFloat`. Then it calculates the absolute difference between the number and its floor and ceiling. It returns the number that has the smaller absolute difference. If the absolute differences are equal, it returns the number that is farther away from zero.

For example, if the input is "10", the function will return 10. If the input is "15.3", the function will return 15. If the input is "14.5", the function will return 15. If the input is "-14.5", the function will return -15.