let count = 0;
for(let i = 0; i < s.length; i += 2) {
  if('AEIOU'.includes(s[i])) {
    count++;
  }
}
return count;
}

console.log(countUpper('aBCdEf')); // 1
console.log(countUpper('abcdefg')); // 0
console.log(countUpper('dBBE')); // 0

// Output:
// 1
// 0
// 0

// Explanation:
// In 'aBCdEf', only the first character 'B' is at an even index, and it is not uppercase.
// In 'abcdefg', there are no uppercase letters at even indices.
// In 'dBBE', there are no uppercase letters at even indices.
// Hence, the function returns 1, 0, and 0 respectively.
```

## Question 2

```javascript
