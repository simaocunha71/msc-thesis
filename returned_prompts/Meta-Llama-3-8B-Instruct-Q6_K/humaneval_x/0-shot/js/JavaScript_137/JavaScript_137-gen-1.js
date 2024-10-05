Here is a JavaScript function that fulfills the requirements:

```javascript
const compareOne = (a, b) => {
  if (typeof a === 'number' && typeof b === 'number') {
    if (a > b) return a;
    if (a < b) return b;
    return null;
  } else if (typeof a === 'string' && typeof b === 'string') {
    a = parseFloat(a.replace(',', '.'));
    b = parseFloat(b.replace(',', '.'));
    if (a > b) return a;
    if (a < b) return b;
    return null;
  } else if (typeof a === 'number' && typeof b === 'string') {
    a = parseFloat(a);
    b = parseFloat(b.replace(',', '.'));
    if (a > b) return a;
    if (a < b) return b;
    return null;
  } else if (typeof a === 'string' && typeof b === 'number') {
    a = parseFloat(a.replace(',', '.'));
    b = parseFloat(b);
    if (a > b) return a;
    if (a < b) return b;
    return null;
  } else {
    return null;
  }
};
```

This function first checks if both inputs are numbers. If they are, it compares them and returns the larger one. If they are not, it checks if both inputs are strings. If they are, it parses the strings as numbers and compares them. If they are not both numbers or strings, it returns null. The function also handles the case where a string represents a real number with a comma instead of a decimal point, by replacing the comma with a decimal point before parsing the string as a number.