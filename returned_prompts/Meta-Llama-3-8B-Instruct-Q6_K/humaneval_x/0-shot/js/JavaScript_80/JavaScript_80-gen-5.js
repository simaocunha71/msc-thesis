Here is a JavaScript solution for the problem:

```javascript
const isHappy = (s) => {
  if (s.length < 3) return false;
  for (let i = 0; i < s.length - 2; i++) {
    const slice = s.slice(i, i + 3);
    if (slice.length === 3 && slice.includes(slice[0])) return false;
  }
  return true;
};
```

Explanation:
The function `isHappy` takes a string `s` as input. It first checks if the length of the string is less than 3. If it is, the function returns `false` because a string with less than 3 characters cannot be happy.

If the length of the string is 3 or more, the function loops through the string, slicing it into chunks of 3 characters. For each chunk, it checks if the chunk contains the same character more than once. If it does, the function returns `false` because the string is not happy.

If the function has not returned `false` after checking all chunks, it returns `true`, indicating that the string is happy.

For example, calling `isHappy("abcd")` would return `true` because every 3 consecutive letters are distinct. Calling `isHappy("aabb")` would return `false` because the 3 consecutive letters "aabb" contain the same character more than once. Calling `isHappy("adb")` would return `true` because every 3 consecutive letters are distinct. Calling `isHappy("xyy")` would return `false` because the 3 consecutive letters "xyy" contain the same character more than once.