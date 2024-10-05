```
const compareOne = (a, b) => {
  if (typeof a === 'string' && typeof b === 'string') {
    a = parseFloat(a.replace(/,/g, '.')); // remove commas and convert to float
    b = parseFloat(b.replace(/,/g, '.')); // remove commas and convert to float
  } else if (typeof a === 'string') {
    a = parseFloat(a); // convert string to float
  } else if (typeof b === 'string') {
    b = parseFloat(b); // convert string to float
  }
  if (a > b) return a;
  if (b > a) return b;
  return null;
};
``` A function that takes two parameters, a and b. The function first checks if both a and b are strings. If they are, it removes the commas and converts them to floats. If only one of a or b is a string, it converts that string to a float. Then, the function compares the two values and returns the larger one. If the values are equal, it returns null.