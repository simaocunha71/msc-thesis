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
1. First, we check if both inputs are strings. If they are, we replace the commas with empty strings using the `replace()` method and then parse the strings to floats using `parseFloat()`. This is because the problem statement mentions that real numbers can be represented as strings with commas.
2. If only one of the inputs is a string, we parse it to a float using `parseFloat()`.
3. We then compare the floats using the usual comparison operators (`>`, `<`, and `==`). If `a` is greater than `b`, we return `a`. If `a` is less than `b`, we return `b`. If `a` and `b` are equal, we return `null`.