  let balance = 0;

  for(let op of operations) {
    balance += op;
    if(balance < 0) return true;
  }

  return false;
};

console.log(belowZero([1, 2, 3])); // false
console.log(belowZero([1, 2, -4, 5])); // true
console.log(belowZero([100, -50, 25, -150])); // true
console.log(belowZero([100, 50, 25, 150])); // false
```

## 10. Find the Missing Number in an Array

