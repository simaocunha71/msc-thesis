Here is a JavaScript function that solves the problem:
```
const isHappy = (s) => {
  if (s.length < 3) return false;
  for (let i = 0; i < s.length - 2; i++) {
    const trio = s.slice(i, i + 3);
    if (trio.includes(trio[0]) || trio.includes(trio[1]) || trio.includes(trio[2])) {
      return false;
    }
  }
  return true;
};
```
Here's an explanation of the code:

1. We first check if the length of the string is less than 3. If it is, we return `false` because a string with length less than 3 cannot be happy.
2. We then loop through the string, taking slices of length 3 at a time (trios).
3. For each trio, we check if any of the letters