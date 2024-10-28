  let count = 0;
  for(let i = 0; i < string.length; i++){
    count++;
  }
  return count;
};

console.log(strlen('')); // 0
console.log(strlen('abc')); // 3

// This solution works by initializing a count variable to 0 and then incrementing it for each character in the string. After going through all characters, it returns the count which represents the length of the string.
```

### 10. Write a JavaScript function that returns the sum of all the numbers in a given array.
```javascript
