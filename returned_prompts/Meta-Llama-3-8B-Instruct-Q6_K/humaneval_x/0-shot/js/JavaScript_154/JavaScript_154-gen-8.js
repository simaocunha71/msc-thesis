```javascript
const cycpatternCheck = (a, b) => {
  for (let i = 0; i < b.length; i++) {
    let rotated = b.substring(i) + b.substring(0, i);
    if (a.includes(rotated)) {
      return true;
    }
  }
  return false;
};
```


Explanation:
The function `cycpatternCheck` checks if the second word `b` or any of its rotations is a substring in the first word `a`.

It iterates over the length of the second word `b` to generate all possible rotations. For each rotation, it checks if the rotated string is a substring in the first word `a` using the `includes` method. If it finds a match, it returns `true`. If no match is found after checking all rotations, it returns `false`.