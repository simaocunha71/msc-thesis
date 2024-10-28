  if (n < 10) return false;
  if (n % 2 !== 0) return false;

  let count = 0;
  for (let i = 2; i <= n / 2; i += 2) {
    if (n - i < i) break;
    count++;
  }

  return count === 4;
};

console.log(isEqualToSumEven(4)); // false
console.log(isEqualToSumEven(6)); // false
console.log(isEqualToSumEven(8)); // true
console.log(isEqualToSumEven(16)); // true
console.log(isEqualToSumEven(18)); // true
console.log(isEqualToSumEven(20)); // false
console.log(isEqualToSumEven(22)); // false
console.log(isEqualToSumEven(24)); // true
console.log(isEqualToSumEven(26)); // false
```

## 10. Calculate the sum of digits of a number

