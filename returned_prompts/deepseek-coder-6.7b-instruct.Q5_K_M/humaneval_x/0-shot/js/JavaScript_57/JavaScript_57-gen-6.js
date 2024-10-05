  const [first, ...rest] = l;

  const isIncreasing = rest.every((n, i) => n > l[i]);
  const isDecreasing = rest.every((n, i) => n < l[i]);

  return isIncreasing || isDecreasing;
}

console.log(monotonic([1, 2, 4, 20])); // true
console.log(monotonic([1, 20, 4, 10])); // false
console.log(monotonic([4, 1, 0, -10])); // true
```

## Problem 3:

Given a list of numbers, write a JavaScript function that returns the sum of all the prime numbers in the list.

```javascript
