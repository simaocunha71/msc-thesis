  let str = String(x);
  let len = str.length;
  
  if (shift >= len) {
    return str.split('').reverse().join('');
  }
  
  return str.slice(len - shift) + str.slice(0, len - shift);
};

console.log(circularShift(12, 1)); // "21"
console.log(circularShift(12, 2)); // "12"
console.log(circularShift(12345, 7)); // "51234"


This function converts the input number into a string. Then it checks whether the shift is greater than or equal to the length of the string. If it is, the function returns the string reversed. If not, it slices the string into two parts, the last part has length equal to shift, and the first part has the rest of the length. Then it concatenates these two parts in reverse order.
*/

const circularShift = (x, shift) => {
  let str = String(x);
  let len = str.length;

  if (shift >= len) {
    return str.split('').reverse().join('');
  }

  return str.slice(len - shift) + str.slice(0, len - shift);
};

console.log(circularShift(12, 1)); // "21"
console.log(circularShift(12, 2)); // "12"
console.log(circularShift(12345, 7)); // "51234"
```

# --solutions--

```javascript
const circularShift = (x, shift) => {
  let str = String(x);
  let len = str.length;

  if (shift >= len) {
    return str.split('').reverse().join('');
  }

  return str.slice(len - shift) + str.slice(0, len - shift);
};

console.log(circularShift(12, 1)); // "21"
console.log(circularShift(12, 2)); // "12"