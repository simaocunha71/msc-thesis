  // If the input list is empty, return 0.
  if (lst.length === 0) {
    return 0;
  }

  let sum = 0;

  for (let i = 0; i < lst.length; i++) {
    // Ignore negative numbers and non-integers.
    if (lst[i] > 0 && Number.isInteger(lst[i])) {
      // If the number is odd, add its square to the sum.
      if (lst[i] % 2 === 1) {
        sum += lst[i] ** 2;
      }
    }
  }

  return sum;
};

console.log(doubleTheDifference([1, 3, 2, 0])); // 10
console.log(doubleTheDifference([-1, -2, 0])); // 0
console.log(doubleTheDifference([9, -2])); // 81
console.log(doubleTheDifference([0])); // 0
console.log(doubleTheDifference([])); // 0

module.exports = doubleTheDifference;
```

## Problem 9 - isPalindrome(str)

```javascript
