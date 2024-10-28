  if(n == 1 && x != 1) {
    return false;
  }

  if(n == 0 && x != 0) {
    return false;
  }

  while(x > 1) {
    x /= n;
  }

  return x === 1;
};

console.log(isSimplePower(1, 4)); // => true
console.log(isSimplePower(2, 2)); // => true
console.log(isSimplePower(8, 2)); // => true
console.log(isSimplePower(3, 2)); // => false
console.log(isSimplePower(3, 1)); // => false
console.log(isSimplePower(5, 3)); // => false
```

## 💻 Explanation:

This program checks if a given number is a simple power of another given number. It does this by continuously dividing the input number by the base number until the number is no longer greater than 1. If the final result is 1, then the input number is a simple power of the base number.

## 🏆 Complexity:

This solution is O(log(n)) because in worst case we are dividing the number n by 2 until it becomes 1.

## 🧩 Test Cases:

Here are some test cases:

```javascript
console.log(isSimplePower(1, 4)); // => true
console.log(isSimplePower(2, 2)); // => true
console.log(isSimplePower(8, 2)); // => true
console.log(isSimplePower(3, 2)); // => false
console.log(isSimplePower(3, 1)); // => false
console.log(isSimplePower(5, 3)); // => false
```

## 📝 Note:

This solution assumes that the input number and base number are positive integers. It does not handle cases where the base number is 0 or 1, as these are edge cases that do not typically apply to powers of numbers.

## 👏 Thanks:

Thank you for reading this solution. I hope it helps you understand how to solve this problem. If you have any further questions, feel