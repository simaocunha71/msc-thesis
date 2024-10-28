  numbers.sort((a, b) => a - b);
  for(let i = 0; i < numbers.length - 1; i++) {
    if(Math.abs(numbers[i] - numbers[i + 1]) < threshold) {
      return true;
    }
  }
  return false;
}

console.log(hasCloseElements([1.0, 2.0, 3.0], 0.5)); // false
console.log(hasCloseElements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)); // true

```

## Problem 3:

```javascript
