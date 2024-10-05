  let charMap = {};
  let count = 0;

  for (let char of string.toLowerCase()) {
    if (!charMap[char]) {
      charMap[char] = true;
      count++;
    }
  }

  return count;
}

console.log(countDistinctCharacters('xyzXYZ')); // 3
console.log(countDistinctCharacters('Jerry')); // 4

// This program works by creating an empty object, charMap, and setting each unique character in the string as a key in the object with a value of true. It then counts the keys in the object to get the number of unique characters.
```

### 2. Write a JavaScript function that will return the sum of all the numbers in an array.

```javascript
