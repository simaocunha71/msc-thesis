  let result = [];
  
  // Swap a and b if a is greater than b
  if (a > b) {
    let temp = a;
    a = b;
    b = temp;
  }
  
  // Loop from a to b
  for (let i = a; i <= b; i++) {
    // Check if i is even
    if (i % 2 === 0) {
      // If so, push it to result array
      result.push(i);
    }
  }
  
  return result;
}

console.log(generateIntegers(2, 8)); // [2, 4, 6, 8]
console.log(generateIntegers(8, 2)); // [2, 4, 6, 8]
console.log(generateIntegers(10, 14)); // []

```

### Solution:

```javascript
