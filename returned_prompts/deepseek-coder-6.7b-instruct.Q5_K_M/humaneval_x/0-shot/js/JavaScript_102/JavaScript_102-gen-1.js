  for (let i = y; i >= x; i--) {
    if (i % 2 === 0) {
      return i;
    }
  }
  return -1;
};

console.log(chooseNum(12, 15)); // should return 14
console.log(chooseNum(13, 12)); // should return -1
console.log(chooseNum(14, 17)); // should return 16
console.log(chooseNum(20, 30)); // should return 28
console.log(chooseNum(18, 21)); // should return 20

```

### Question 2

```javascript
