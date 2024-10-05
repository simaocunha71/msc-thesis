  let balance = 0;

  for (let operation of operations) {
    balance += operation;
    if (balance < 0) {
      return true;
    }
  }

  return false;
}

console.log(belowZero([1, 2, 3])); // false
console.log(belowZero([1, 2, -4, 5])); // true
console.log(belowZero([100, -50, -75])); // true
console.log(belowZero([100, -50, 50, -25])); // false

// The function iterates over the provided operations array and adds each value to the balance. 
// If at any point the balance is less than zero, the function immediately returns true. 
// If no such point is found after all operations, the function returns false.
```

#### 2. Check if array is sorted

```javascript
