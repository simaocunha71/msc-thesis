Here is the solution using JavaScript:

```javascript
const encode = (message) => {
  const vowels = 'aeiouAEIOU';
  const result = [];

  for (let char of message) {
    if (vowels.includes(char)) {
      const index = vowels.indexOf(char);
      result.push(String.fromCharCode(index + 2));
    } else if (char === char.toUpperCase()) {
      result.push(char.toLowerCase());
    } else {
      result.push(char.toUpperCase());
    }
  }
  return result.join('');
};
```

Explanation:

1. We first define a string `vowels` that contains all the vowels (both lowercase and uppercase).
2. We initialize an empty array `result` that will store the encoded characters.
3. We iterate over each character `char` in the input `message` using a `for...of` loop.
4. If the character is a vowel, we find its index in the `vowels` string using `indexOf`. We then use `String.fromCharCode` to get the character that is 2 positions ahead of the current vowel in the alphabet. We add this character to the `result` array.
5. If the character is not a vowel, we check if it's uppercase. If it is, we convert it to lowercase and add it to the `result` array. If it's not uppercase, we convert it to uppercase and add it to the `result` array.
6. Finally, we join the `result` array into a string using `join` and return the encoded message.