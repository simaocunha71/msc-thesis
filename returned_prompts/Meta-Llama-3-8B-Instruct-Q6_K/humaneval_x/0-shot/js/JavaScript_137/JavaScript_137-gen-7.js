```
const compareOne = (a, b) => {
  if (typeof a === 'string' && typeof b === 'string') {
    a = parseFloat(a.replace(',', ''));
    b = parseFloat(b.replace(',', ''));
  } else if (typeof a === 'string') {
    a = parseFloat(a);
  } else if (typeof b === 'string') {
    b = parseFloat(b);
  }
  
  if (a > b) return a;
  else if (a < b) return b;
  else return null;
};
```


Explanation:

1. We start by checking if both `a` and `b` are strings. If they are, we replace the comma (if present) with an empty string and convert the resulting string to a float using `parseFloat()`. This allows us to compare the numbers correctly.
2. If only one of `a` or `b` is a string, we convert it to a float using `parseFloat()`. This ensures that both values are of the same type (either both numbers or both strings).
3. We then compare the two values using simple conditional statements. If `a` is greater than `b`, we return `a`. If `a` is less than `b`, we return `b`. If the values are equal, we return `null`.