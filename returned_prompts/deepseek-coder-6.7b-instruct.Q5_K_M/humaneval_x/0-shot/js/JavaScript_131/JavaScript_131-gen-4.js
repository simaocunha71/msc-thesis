  const digitsArr = Array.from(String(n), Number);
  const oddDigits = digitsArr.filter(digit => digit % 2 !== 0);

  if (oddDigits.length === 0) {
    return 0;
  } else {
    return oddDigits.reduce((acc, cur) => acc * cur);
  }
};

console.log(digits(1));
console.log(digits(4));
console.log(digits(235));


```

### Solution

```javascript

