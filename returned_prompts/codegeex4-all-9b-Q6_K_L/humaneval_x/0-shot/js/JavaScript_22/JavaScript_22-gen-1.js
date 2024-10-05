You can use the `filter()` function in combination with a `typeof` operator to accomplish this. Here's how you can do it:

```javascript
const filterIntegers = (values) => {
  return values.filter(value => typeof value === 'number' && Number.isInteger(value));
};
```

This code will return a new array that only includes the integers from the original array. The `filter()` function is used to iterate over each value in the array, and the `typeof` operator checks if the value is a number. The `Number.isInteger()` function checks if the number is an integer.

The `filter()` function returns a new array that only includes the values that pass the test implemented by the provided function.