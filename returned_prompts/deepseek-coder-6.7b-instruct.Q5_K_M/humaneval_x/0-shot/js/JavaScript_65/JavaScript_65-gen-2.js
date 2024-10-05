  const digits = String(x).split('');
  const len = digits.length;

  if (shift >= len) {
    return digits.reverse().join('');
  }

  const shifted = digits.slice(len - shift).concat(digits.slice(0, len - shift));
  return shifted.join('');
};

console.log(circularShift(12, 1)); // "21"
console.log(circularShift(12, 2)); // "12"
console.log(circularShift(12345, 3)); // "34512"
console.log(circularShift(12345, 6)); // "54321"
```

# Exercise 2

```js
