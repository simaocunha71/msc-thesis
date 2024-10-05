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

  if (a > b) {
    return a;
  } else if (a < b) {
    return b;
  } else {
    return null;
  }
};
```


Explanation:

1. First, check if both `a` and `b` are strings. If they are, replace the comma (if present) with an empty string and convert the strings to floating point numbers using `parseFloat`.
2. If `a` is a string but `b` is not, convert `a` to a floating point number using `parseFloat`.
3. If `b` is a string but `a` is not, convert `b` to a floating point number using `parseFloat`.
4. Compare `a` and `b` using the `>` and `<` operators. If `a` is greater than `b`, return `a`. If `a` is less than `b`, return `b`. If `a` is equal to `b`, return `null`.