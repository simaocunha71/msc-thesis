  if (!strings.length) return null;
  let longest = "";
  for (let i = 0; i < strings.length; i++) {
    if (strings[i].length > longest.length) {
      longest = strings[i];
    }
  }
  return longest;
};

console.log(longest([])); // null
console.log(longest(['a', 'b', 'c'])); // 'a'
console.log(longest(['a', 'bb', 'ccc'])); // 'ccc'

```

## 2. Counting Vowels

Write a function that takes a string as input and returns the count of vowels in it.

