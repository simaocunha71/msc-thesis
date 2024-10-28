  return strings.filter(str => str.includes(substring))
}

console.log(filterBySubstring([], 'a')) // []
console.log(filterBySubstring(['abc', 'bacd', 'cde', 'array'], 'a')) // ['abc', 'bacd', 'array']
```

## Problem 3

Write a function that takes an object and a value, and returns the keys of the object that map to the given value.

