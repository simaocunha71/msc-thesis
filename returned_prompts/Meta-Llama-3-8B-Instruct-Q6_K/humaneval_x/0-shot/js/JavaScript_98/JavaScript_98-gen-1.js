The problem can be solved by iterating over the string and checking if the character at even indices is uppercase and a vowel. Here is the JavaScript function that implements this:

```javascript
const countUpper = (s) => {
  let count = 0;
  for (let i = 0; i < s.length; i++) {
    if (i % 2 === 0 && /[AEIOU]/i.test(s[i])) {
      count++;
    }
  }
  return count;
};
```

In this function, we initialize a variable `count` to 0. Then we iterate over the string using a for loop. For each character, we check if the index is even (`i % 2 === 0`) and if the character is an uppercase vowel (`/[AEIOU]/i.test(s[i])`). If both conditions are true, we increment the `count`. Finally, we return the `count`. The `/[AEIOU]/i` is a regular expression that matches any uppercase or lowercase vowel. The `i` at the end of the regular expression makes it case-insensitive.