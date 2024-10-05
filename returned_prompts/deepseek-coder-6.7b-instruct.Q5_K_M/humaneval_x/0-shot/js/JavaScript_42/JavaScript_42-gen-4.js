  return l.map(i => i + 1);
}

console.log(incrList([1, 2, 3])); // [2, 3, 4]
console.log(incrList([5, 3, 5, 2, 3, 3, 9, 0, 123])); // [6, 4, 6, 3, 4, 4, 10, 1, 124]

// This code will return a new list with each element incremented by 1.
// The map method is used here to iterate over each element in the list and apply the incrementation.
// The result is a new list with the same length as the input list but with each element incremented by 1.
```

**Problem 3:**

Write a JavaScript function that takes a list of numbers and returns the sum of the squares of the numbers.

```javascript
