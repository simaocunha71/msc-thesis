```
const compareOne = (a, b) => {
  if (typeof a === 'number' && typeof b === 'number') {
    if (a > b) return a;
    else if (a < b) return b;
    else return null;
  } else if (typeof a === 'string' && typeof b === 'string') {
    a = a.replace(/,/g, '.');
    b = b.replace(/,/g, '.');
    if (parseFloat(a) > parseFloat(b)) return a;
    else if (parseFloat(a) < parseFloat(b)) return b;
    else return null;
  } else if (typeof a === 'number' && typeof b === 'string') {
    a = a.toString();
    a = a.replace(/,/g, '.');
    if (parseFloat(a) > parseFloat(b)) return a;
    else if (parseFloat(a) < parseFloat(b)) return b;
    else return null;
  } else if (typeof a === 'string' && typeof b === 'number') {
    b = b.toString();
    b = b.replace(/,/g, '.');
    if (parseFloat(a) > parseFloat(b)) return a;
    else if (parseFloat(a) < parseFloat(b)) return b;
    else return null;
  }
};
```


This function checks the types of both input arguments, then compares them accordingly. If both are numbers, it simply returns the larger one. If both are strings (representing numbers), it replaces the commas with dots, then compares them as numbers. If one is a number and the other is a string, it converts the number to a string, replaces the commas with dots, then compares them as strings. If the values are equal, it returns null.