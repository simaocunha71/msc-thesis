  const counter = (string) => string.split('').reduce((acc, char) => {
    acc[char] = (acc[char] || 0) + 1;
    return acc;
  }, {});

  const countS0 = counter(s0);
  const countS1 = counter(s1);

  if (Object.keys(countS0).length !== Object.keys(countS1).length) {
    return false;
  }

  for (let char in countS0) {
    if (countS0[char] !== countS1[char]) {
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
```

This code defines a function `sameChars` that checks if two strings have the same characters and the same quantities of each character. It does this by first creating a count object for each string using the `counter` function, which converts each string into an object where the keys are the characters and the values are the counts of those characters. It then checks if the count objects have the same keys and the same values for each key, returning `true` if they do and `false` otherwise.

This solution has a time complexity of O(n), where n is the length of the shorter string, because it iterates over the strings once. Its space complexity is also O(n), because it creates a count object for each string.

I hope this solution is helpful for you. If you have any other questions, feel free to ask.


























