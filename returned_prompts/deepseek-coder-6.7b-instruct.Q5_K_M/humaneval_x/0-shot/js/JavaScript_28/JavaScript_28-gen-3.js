  return strings.join('');
};

console.log(concatenate([])); // ''
console.log(concatenate(['a', 'b', 'c'])); // 'abc'

// Explanation:
// The `join()` method is a built-in JavaScript function that combines all elements of an array into a single string. In this case, it is used to concatenate an array of strings into a single string.
// The `join()` method takes a parameter, a string that is used as a separator between elements of the array. In this case, an empty string (''), which means no separator is used.
// The `concatenate()` function takes an array of strings as its argument and returns the result of the `join()` method, which is a single string that includes all the strings from the array.
```

## 7. Reduce

```javascript
