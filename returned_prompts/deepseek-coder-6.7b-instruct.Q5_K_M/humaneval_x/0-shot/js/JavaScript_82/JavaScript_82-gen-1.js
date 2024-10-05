let length = string.length;

  if (length < 2) {
    return false;
  }

  for (let i = 2, sqrt = Math.sqrt(length); i <= sqrt; i++) {
    if (length % i === 0) {
      return false;
    }
  }

  return true;

};

console.log(primeLength('Hello')); // true
console.log(primeLength('abcdcba')); // true
console.log(primeLength('kittens')); // true
console.log(primeLength('orange')); // false
```

## Problem 7

```javascript
