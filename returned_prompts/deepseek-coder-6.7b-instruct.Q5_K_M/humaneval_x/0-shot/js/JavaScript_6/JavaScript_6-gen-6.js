  const parenArray = paren_string.split(' ');
  const result = [];

  for (let parenGroup of parenArray) {
    let count = 0;
    let max = 0;
    for (let char of parenGroup) {
      if (char === '(') {
        count += 1;
        if (count > max) {
          max = count;
        }
      } else if (char === ')') {
        count -= 1;
      }
    }
    result.push(max);
  }

  return result;
}

parseNestedParens('(()())  ((()))  ()  ((())()())');
```

## 2. Write a function that calculates the difference of the sum of two diagonal elements in a square matrix.

