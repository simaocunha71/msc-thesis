  if (strings.length === 0) return null;

  let longest = "";
  for (let i = 0; i < strings.length; i++) {
    if (strings[i].length > longest.length) {
      longest = strings[i];
    }
  }
  return longest;
};

console.log(longest([]));
console.log(longest(['a', 'b', 'c']));
console.log(longest(['a', 'bb', 'ccc']));
```

Here's the JavaScript code that implements the given problem:

```javascript
// Problem: Longest String
// Given a list of strings, return the longest string in the list. 
// If there are multiple strings of the same maximum length, return the first one. 
// If the list is empty, return null.

// 