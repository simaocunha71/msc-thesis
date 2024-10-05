  const nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
  return numbers.split(' ').sort((a, b) => nums.indexOf(a) - nums.indexOf(b)).join(' ');
}

console.log(sortNumbers('three one five')); // Outputs: 'one three five'
```

## 6. Reverse a String

```javascript
