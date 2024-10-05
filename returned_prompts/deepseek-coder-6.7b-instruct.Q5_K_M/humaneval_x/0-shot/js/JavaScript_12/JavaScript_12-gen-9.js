  if(strings.length === 0) {
    return null;
  }

  let longestString = strings[0];
  let maxLength = strings[0].length;

  for(let i = 1; i < strings.length; i++) {
    if(strings[i].length > maxLength) {
      longestString = strings[i];
      maxLength = strings[i].length;
    }
  }

  return longestString;
}

console.log(longest([])); // null
console.log(longest(['a', 'b', 'c'])); // 'a'
console.log(longest(['a', 'bb', 'ccc'])); // 'ccc'
```

## Solution 2

```javascript
