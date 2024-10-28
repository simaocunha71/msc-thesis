Here is a JavaScript solution for the problem:
```
const checkIfLastCharIsALetter = (txt) => {
  if (txt.length === 0) return false;
  const lastChar = txt.slice(-1);
  return /^[a-zA-Z]$/.test(lastChar) && !/\s/.test(txt.slice(-1));
};
```
Here's an explanation of the code:

1. We first check if the input string `txt` is empty. If it is, we immediately return `false`.
2. We use the `slice(-1)` method to get the last character of the string.
3. We use a regular expression `^[a-zA-Z]$` to check if the last character is an alphabetical character (either uppercase or lowercase). The `^` symbol matches the start of the string, `[a-zA-Z]` matches any alphabetical character, and `$` matches the end of the string. The `test()` method returns a boolean value indicating whether the regular expression matches the last character.
4. We also use another regular expression `/\s/.test(txt.slice(-1))` to check if the last character is a whitespace character. The `/\s/` regular expression matches any whitespace character, and the `test()` method returns a boolean value indicating whether the regular expression matches the last character.
5. We use the logical `&&` operator to combine the two conditions. If both conditions are true, we return `true`; otherwise, we return `false`.

You can test the function with the examples provided in the problem statement to see that it returns the expected results.