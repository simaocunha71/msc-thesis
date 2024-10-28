Here is a possible implementation of the `histogram` function in JavaScript:
```
const histogram = (test) => {
  const letterCounts = {};
  const letters = test.split(' ');

  for (const letter of letters) {
    if (!letterCounts[letter]) {
      letterCounts[letter] = 0;
    }
    letterCounts