  return strings.filter(string => string.startsWith(prefix));
}

// Test cases
console.log(filterByPrefix([], 'a')); // []
console.log(filterByPrefix(['abc', 'bcd', 'cde', 'array'], 'a')); // ['abc', 'array']
```

## Problem 2: Remove Duplicates from a List

Write a function that removes duplicates from an array.

```javascript
