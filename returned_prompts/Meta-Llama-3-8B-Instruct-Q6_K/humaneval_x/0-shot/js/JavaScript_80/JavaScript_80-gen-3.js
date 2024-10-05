```javascript
const isHappy = (s) => {
  if (s.length < 3) return false;
  for (let i = 0; i <= s.length - 3; i++) {
    const first = s[i];
    const second = s[i + 1];
    const third = s[i + 2];
    if (first === second || first === third || second === third) return false;
  }
  return true;
};
```


Explanation:
The function `isHappy` takes a string `s` as an argument. It first checks if the length of the string is less than 3. If it is, the function returns `false`, because a string with a length of less than 3 cannot be happy.

If the length of the string is 3 or more, the function uses a for loop to iterate over the string, checking every 3 consecutive characters. If any 3 consecutive characters are the same, the function returns `false`, because the string is not happy.

If the function iterates over the entire string and does not find any 3 consecutive characters that are the same, it returns `true`, indicating that the string is happy.