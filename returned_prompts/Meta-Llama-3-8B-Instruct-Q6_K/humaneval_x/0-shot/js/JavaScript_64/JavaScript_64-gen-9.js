Here is a possible implementation of the `vowelsCount` function:
```
const vowelsCount = (s) => {
  let count = 0;
  for (let i = 0; i < s.length; i++) {
    const c = s[i].toLowerCase();
    if (c === 'a' || c === 'e' || c === 'i' || c === 'o' || c === 'u') {
      count++;
    } else if (c === 'y' && i === s.length - 1) {
      count++;
    }
  }
  return count;
};
```
Here's an explanation of how the function works:

1. We initialize a variable `count` to 0, which will keep track of the number of vowels in the string.
2. We iterate over each character `c` in the input string `s` using a `for` loop.
3. For each character, we convert it to lowercase using the `toLowerCase()` method, so that we can compare it with the vowels in a case-insensitive way.
4. We check if the character is one of the vowels (`a`, `e`, `i`, `o`, or `u`). If it is, we increment the `count` variable.
5. We also check if the character is `y` and if it is the last character in the string. If it is, we increment the `count` variable, since `y` is a vowel at the end of a word.
6. Finally, we return the `count` variable at the end of the function.

You can test this function with the examples you provided:
```
console.log(vowelsCount("abcde")); // Output: 2
console.log(vowelsCount("ACEDY")); // Output: 3
```
I hope this helps! Let me know if you have any questions. 😊

Note: This implementation assumes that the input string only contains ASCII characters. If you need to support non-ASCII characters, you may need to modify the implementation accordingly.