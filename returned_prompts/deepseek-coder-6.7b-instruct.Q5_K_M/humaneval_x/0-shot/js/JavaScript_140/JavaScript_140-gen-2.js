  return text.replace(/\s{2,}/g, '-').replace(/\s/g, '_');

};

console.log(fixSpaces("Example")) // "Example"
console.log(fixSpaces("Example 1")) // "Example_1"
console.log(fixSpaces(" Example 2")) // "_Example_2"
console.log(fixSpaces(" Example  3")) // "_Example-3"

```

### 5. Replace all occurrences of a character in a string

