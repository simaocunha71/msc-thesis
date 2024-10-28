```
const encode = (message) => {
  const vowels = 'aeiouAEIOU';
  return message
    .split('')
    .map((char) => {
      if (vowels.includes(char)) {
        const index = vowels.indexOf(char);
        const nextIndex = (index + 2) % vowels.length;
        return vowels.charAt(nextIndex);
      }
      return char === char.toUpperCase()
        ? char.toLowerCase()
        : char.toUpperCase();
    })
    .join('');
};
```



Explanation:

1. First, we define a string `vowels` that contains all the vowels in both lowercase and uppercase.
2. We use the `split` method to split the input `message` into an array of individual characters.
3. We use the `map` method to iterate over the array of characters. For each character:
   - If the character is a vowel, we find its index in the `vowels` string and calculate the index of the next vowel (2 positions ahead). We use the modulo operator (`%`) to ensure that the index wraps around to the beginning of the string if it exceeds the length of the string.
   - If the character is not a vowel, we simply swap its case using the ternary operator.
4. Finally, we use the `join` method to concatenate the modified characters back into a string.

The function returns the encoded message.