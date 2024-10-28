  const nums = [...n.toString()];
  let product = 1;
  let found = false;

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] % 2 !== 0) {
      found = true;
      product *= parseInt(nums[i]);
    }
  }

  return found ? product : 0;
}

console.log(digits(1));  // 1
console.log(digits(4));  // 0
console.log(digits(235));  // 15
console.log(digits(23456789));  // 1511
console.log(digits(23456781));  // 1
```

## 2. Array to String

