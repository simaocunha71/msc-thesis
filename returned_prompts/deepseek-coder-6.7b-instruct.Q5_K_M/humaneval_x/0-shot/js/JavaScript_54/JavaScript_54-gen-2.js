  const countChars = (str) => str.split('').reduce((acc, char) => {
    acc[char] = (acc[char] || 0) + 1;
    return acc;
  }, {});

  const count0 = countChars(s0);
  const count1 = countChars(s1);

  if (Object.keys(count0).length !== Object.keys(count1).length) {
    return false;
  }

  for (let char in count0) {
    if (count0[char] !== count1[char]) {
      return false;
    }
  }

  return true;
};

console.log(sameChars('eabcdzzzz', 'dddzzzzzzzddeddabc')); // true
console.log(sameChars('abcd', 'dddddddabc')); // true
console.log(sameChars('dddddddabc', 'abcd')); // true
console.log(sameChars('eabcd', 'dddddddabc')); // false
console.log(sameChars('abcd', 'dddddddabce')); // false
console.log(sameChars('eabcdzzzz', 'dddzzzzzzzddddabc')); // false

// Time complexity: O(n + m)
// Space complexity: O(n + m)
// n and m are the lengths of the two strings.
// This is because we traverse each string once to count the characters, and we store the counts in a hash map.
```

---

## The problem

Check if two words have the same characters.

## The solution

```javascript
const sameChars = (s0, s1) => {
  const countChars = (str) => str.split('').reduce((acc, char) => {
    acc[char] = (acc[char] || 0) + 1;
    return acc;
  }, {});

  const count0 = countChars(s0);
  const count1 = countChars(s1);

  if (Object.keys(count0).length !== Object.keys(count1