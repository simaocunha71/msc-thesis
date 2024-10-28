  if (s.length < 3) {
    return false;
  }
  for (let i = 0; i < s.length - 2; i++) {
    if (s[i] === s[i + 1] || s[i] === s[i + 2] || s[i + 1] === s[i + 2]) {
      return false;
    }
  }
  return true;
}
```
These are the solutions to the given problems in JavaScript. The solutions cover various topics such as array manipulation, string processing, and numerical operations. They also involve logical conditions and loop constructs to achieve the desired results. If you have any further questions or need clarification on any of the solutions, feel free to ask!