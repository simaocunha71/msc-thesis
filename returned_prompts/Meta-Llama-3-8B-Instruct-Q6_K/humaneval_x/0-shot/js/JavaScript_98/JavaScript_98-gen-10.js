Here is the JavaScript code to solve the problem:
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
Explanation:

* We initialize a variable `count` to 0 to keep track of the number of uppercase vowels in even indices.
* We iterate through the string `s` using a for loop.
* For each character at index `i`, we check if it is at an even index (`i % 2 === 0`) and if it is an uppercase vowel using the regex `/[AEIOU]/i.test(s[i])`. The `i` flag makes the regex case-insensitive.
* If the character is at an even index and is an uppercase vowel, we increment the `count` variable.
* Finally, we return the `count` variable at the end of