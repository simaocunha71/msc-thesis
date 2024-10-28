You can solve this problem by checking if the given number is divisible by 2 and if the quotient is greater than or equal to 4. Here is an example of how you can do it in JavaScript:

```javascript
const isEqualToSumEven = (n) => {
  // Check if the number is even
  if (n % 2 === 0) {
    // Divide the number by 2
    const quotient = n / 2;
    // Check if the quotient is greater than or equal to 4
    if (quotient >= 4) {
      return true;
    }
  }
  return false;
};

console.log(isEqualToSumEven(4)); // false
console.log(isEqualToSumEven(6)); // false
console.log(isEqualToSumEven(8)); // true
```

This function works by first checking if the given number is even. If it is, the function divides the number by 2 and checks if the quotient is greater than or equal to 4. If both conditions are true, the function returns true, indicating that the given number can be written as the sum of exactly 4 positive even numbers. If either condition is false, the function returns false.