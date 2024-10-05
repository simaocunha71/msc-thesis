  const sortedS0 = [...s0].sort().join('');
  const sortedS1 = [...s1].sort().join('');
  return sortedS0 === sortedS1;
}

console.log(sameChars('eabcdzzzz', 'dddzzzzzzzddeddabc')); // true
console.log(sameChars('abcd', 'dddddddabc')); // true
console.log(sameChars('dddddddabc', 'abcd')); // true
console.log(sameChars('eabcd', 'dddddddabc')); // false
console.log(sameChars('abcd', 'dddddddabce')); // false
console.log(sameChars('eabcdzzzz', 'dddzzzzzzzddddabc')); // false

```

```javascript
// Solution 2
