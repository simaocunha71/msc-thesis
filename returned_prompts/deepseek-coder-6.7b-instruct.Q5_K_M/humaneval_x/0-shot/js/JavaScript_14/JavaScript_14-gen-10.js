  let result = [];

  for (let i = 0; i < string.length; i++) {
    result.push(string.slice(0, i + 1));
  }

  return result;
};

console.log(allPrefixes('abc'));

// Output: [ 'a', 'ab', 'abc' ]
```

### Solution 2:

```javascript
