  let result = [];

  // Swap the numbers if a is greater than b
  if (a > b) {
    let temp = a;
    a = b;
    b = temp;
  }

  // Iterate through the range from a to b
  for (let i = a; i <= b; i++) {
    // Check if the digit is even
    if (i % 2 === 0) {
      // Add the digit to the result
      result.push(i);
    }
  }

  return result;
}

console.log(generateIntegers(2, 8));
console.log(generateIntegers(8, 2));
console.log(generateIntegers(10, 14));
```


```javascript
