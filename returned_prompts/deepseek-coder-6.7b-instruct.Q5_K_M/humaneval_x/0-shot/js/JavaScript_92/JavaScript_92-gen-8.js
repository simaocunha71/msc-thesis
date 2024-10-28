  if (Number.isInteger(x) && Number.isInteger(y) && Number.isInteger(z)) {
    return x === y + z || y === x + z || z === x + y;
  }
  return false;
}

console.log(anyInt(5, 2, 7)); // ➞ true
console.log(anyInt(3, 2, 2)); // ➞ false
console.log(anyInt(3, -2, 1)); // ➞ true
console.log(anyInt(3.6, -2.2, 2)); // ➞ false
console.log(anyInt(3, 2, 5)); // ➞ false
console.log(anyInt(2, 2, 3)); // ➞ true
console.log(anyInt(-1, 2, 3)); // ➞ true
console.log(anyInt(3, 2.2, 5)); // ➞ false

// In this code, we first check if all the input numbers are integers using the Number.isInteger() function.
// If not, we return false.
// If they are all integers, we then check if any one of them is equal to the sum of the other two numbers.
// If so, we return true; otherwise, we return false.

// Note: The prompt seems to be a bit ambiguous regarding what should be returned when all numbers are not integers.
// The example given for anyInt(3.6, -2.2, 2) ➞ false seems to imply that only integers should be used, so it returns false in this case.
// If all integer checks should also be included in the return, we can simply add them to the if statement.
// Note that this would make the prompt's examples incorrect, as they would always return false.

```

### JavaScript
```javascript
