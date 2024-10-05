  let totalChars1 = lst1.join("").length;
  let totalChars2 = lst2.join("").length;

  return totalChars1 < totalChars2 ? lst1 : lst2;
}

// Test cases
console.log(totalMatch([], [])); // ➞ []
console.log(totalMatch(["hi", "admin"], ["hI", "Hi"])); // ➞ ["hI", "Hi"]
console.log(totalMatch(["hi", "admin"], ["hi", "hi", "admin", "project"])); // ➞ ["hi", "admin"]
console.log(totalMatch(["hi", "admin"], ["hI", "hi", "hi"])); // ➞ ["hI", "hi", "hi"]
console.log(totalMatch(["4"], ["1", "2", "3", "4", "5"])); // ➞ ["4"]

// Explanation:
// The total number of chars in the first list is 11 (hi + admin = 2 + 3)
// The total number of chars in the second list is 10 (hI + hi + hi = 2 + 2 + 2)
// The first list has a lesser number of chars so it is returned.
```

## Answer:

```javascript
const totalMatch = (lst1, lst2) => {
  let totalChars1 = lst1.join("").length;
  let totalChars2 = lst2.join("").length;

  return totalChars1 < totalChars2 ? lst1 : lst2;
}

// Test cases
console.log(totalMatch([], [])); // ➞ []
console.log(totalMatch(["hi", "admin"], ["hI", "Hi"])); // ➞ ["hI", "Hi"]
console.log(totalMatch(["hi", "admin"], ["hi", "hi", "admin", "project"])); // ➞ ["hi", "admin"]
console.log(totalMatch(["hi", "admin"], ["hI", "hi", "hi"])); // 