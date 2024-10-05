To solve this kata, we can define a function called `compareOne` that takes two parameters, `a` and `b`. These parameters can be integers, floats, or strings representing real numbers. The function will return the larger variable in its given variable type, and `null` if the values are equal.

To compare the values, we can use conditional (ternary) operators to check if `a` is less than `b`, equal to `b`, or greater than `b`. If `a` is less than `b`, we can convert `b` to a string and return it. If `a` is equal to `b`, we can return `null`. If `a` is greater than `b`, we can convert `a` to a string and return it.

To handle the case where `a` and `b` are both strings, we can use the `parseFloat()` method to convert the strings to floating point numbers and then compare them using the same logic as above.

Here's the complete solution in JavaScript:

```javascript
const compareOne = (a, b) => {
  if (typeof a === 'string' && typeof b === 'string') {
    const aFloat = parseFloat(a);
    const bFloat = parseFloat(b);
    if (aFloat === bFloat) {
      return null;
    } else if (aFloat > bFloat) {
      return a;
    } else {
      return b;
    }
  } else if (typeof a === 'string') {
    const aFloat = parseFloat(a);
    if (aFloat === b) {
      return null;
    } else {
      return aFloat.toString();
    }
  } else if (typeof b === 'string') {
    const bFloat = parseFloat(b);
    if (a === bFloat) {
      return null;
    } else {
      return bFloat.toString();
    }
  } else {
    if (a > b) {
      return a.toString();
    } else if (a < b) {
      return b.toString();
    } else {
      return null;
    }
  }
};
```

You can test the function using the provided test