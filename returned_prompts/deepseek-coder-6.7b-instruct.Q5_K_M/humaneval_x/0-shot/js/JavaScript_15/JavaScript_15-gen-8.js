  let result = '';
  for (let i = 0; i <= n; i++) {
    result += i + ' ';
  }
  return result.trim();
};

console.log(stringSequence(0)); // '0'
console.log(stringSequence(5)); // '0 1 2 3 4 5'

// This function loops from 0 to n (inclusive), and for each iteration, it adds the current number plus a space to the result string.
// The .trim() at the end is used to remove the trailing space.

// Please, try to solve this problem by your own. If you have any questions, feel free to ask.
```

---

### 5. 

```js
