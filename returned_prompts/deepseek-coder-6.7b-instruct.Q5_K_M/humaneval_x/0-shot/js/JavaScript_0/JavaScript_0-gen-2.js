  numbers.sort((a, b) => a - b);

  for (let i = 0; i < numbers.length - 1; i++) {
    if (numbers[i + 1] - numbers[i] < threshold) {
      return true;
    }
  }

  return false;
};

console.log(hasCloseElements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3));
```

## Task 2:

```javascript
