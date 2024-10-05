  const numbers = Array.from(n.toString()).map(Number);
  const oddNumbers = numbers.filter(num => num % 2 !== 0);
  
  if (oddNumbers.length === 0) {
    return 0;
  } else {
    return oddNumbers.reduce((a, b) => a * b);
  }
};

console.log(digits(235));

// Test cases:
console.log(digits(1));   // 1
console.log(digits(4));   // 0
console.log(digits(235)); // 15
console.log(digits(111)); // 1
console.log(digits(13579)); // 1059
console.log(digits(2468)); // 0

// Convert integer n to string using n.toString()
// Convert string to array using Array.from()
// Convert elements of array to numbers using map(Number)
// Filter out odd numbers using filter()
// If there are no odd numbers, return 0
// If there are odd numbers, return their product using reduce()
```


## 2.
```js
// Exercise 2
