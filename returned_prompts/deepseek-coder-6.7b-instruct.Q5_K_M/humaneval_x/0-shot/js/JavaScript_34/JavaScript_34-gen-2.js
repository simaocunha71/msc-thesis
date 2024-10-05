  return [...new Set(l.sort((a, b) => a - b))];
};

console.log(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]));

// Explanation:
// The Set object lets you store unique values of any type, whether primitive values or object references.
// The sort() method sorts the elements of an array in place and returns the array. The default sort order is built upon converting the elements into strings, then comparing their sequences of UTF-16 code unit values.
// The spread syntax (...) is used to expand an iterable (like an array expression) into zero or more arguments (for function calls) or elements (for array literals).
```

## JavaScript - Sum of all array elements
```javascript
