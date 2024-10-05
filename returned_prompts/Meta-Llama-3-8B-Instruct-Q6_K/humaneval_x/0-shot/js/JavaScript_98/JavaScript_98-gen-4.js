Here is a solution for the problem:
```
const countUpper = (s) => {
  let count = 0;
  for (let i = 0; i < s.length; i++) {
    if (i % 2 === 0 && s[i].toUpperCase() === 'A' || s[i].toUpperCase() === 'E' || s[i].toUpperCase() === 'I' || s[i].toUpperCase() === 'O' || s[i].toUpperCase() === 'U') {
      count++;
    }
  }
  return count;
};
```
Explanation:
The solution iterates through the string `s` using a for loop. For each character, it checks if the index `i` is even (using the condition `i % 2 === 0`). If it is, it checks if the character is an uppercase vowel (using the condition `s[i].toUpperCase() === 'A' || s[i].toUpperCase() === 'E' || s[i].toUpperCase() === 'I' || s[i].toUpperCase() === 'O' || s[i].toUpperCase() === 'U'`). If it is an uppercase vowel, it increments the count variable. Finally, it returns the count.

Note: The `toUpperCase()` method is used to convert the character to uppercase for comparison. This is because the problem statement asks for uppercase vowels, so we need to check if the character is an uppercase vowel, not a lowercase vowel.