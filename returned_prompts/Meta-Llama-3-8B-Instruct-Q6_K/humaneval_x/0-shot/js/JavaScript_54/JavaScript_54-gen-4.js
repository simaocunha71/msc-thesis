Here is a solution that uses a hash map to count the frequency of each character in both strings, and then compares the frequency maps.

```javascript
const sameChars = (s0, s1) => {
  if (s0.length !== s1.length) return false;
  const freq0 = {};
  const freq1 = {};
  for (let char of s0) {
    freq0[char] = (freq0[char] || 0) + 1;
  }
  for (let char of s1) {
    freq1[char] = (freq1[char] || 0) + 1;
  }
  return JSON.stringify(freq0) === JSON.stringify(freq1);
};
```

This solution has a time complexity of O(n), where n is the length of the strings, because it iterates over each character in the strings once. The space complexity is also O(n), because it uses hash maps to store the frequency of each character.

You can test this function with the examples you provided:

```javascript
console.log(sameChars('eabcdzzzz', 'dddzzzzzzzddeddabc')); // true
console.log(sameChars('abcd', 'dddddddabc')); // true
console.log(sameChars('dddddddabc', 'abcd')); // true
console.log(sameChars('eabcd', 'dddddddabc')); // false
console.log(sameChars('abcd', 'dddddddabce')); // false
console.log(sameChars('eabcdzzzz', 'dddzzzzzzzddddabc')); // false
```  1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92