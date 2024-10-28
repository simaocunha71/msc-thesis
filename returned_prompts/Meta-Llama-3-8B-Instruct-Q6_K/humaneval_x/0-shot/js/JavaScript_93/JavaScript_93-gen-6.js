```
const encode = (message) => {
  const vowels = 'aeiou';
  const result = [];
  for (let char of message) {
    if (char === char.toUpperCase()) {
      result.push(char.toLowerCase());
    } else {
      result.push(char.toUpperCase());
    }
    if (vowels.includes(char.toLowerCase())) {
      const index = vowels.indexOf(char.toLowerCase());
      const nextIndex = (index + 2) % vowels.length;
      result.push(vowels.charAt(nextIndex));
    } else {
      result.push(char);
    }
  }
  return result.join('');
};
```
The above function iterates over each character in the message. It checks if the character is uppercase or lowercase and swaps the case accordingly. Then it checks if the character is a vowel. If it is, it finds the next vowel in the alphabet by finding the index of the vowel in the vowels string, adding 2 to it, and taking the remainder when divided by the length of the vowels string to handle wrapping around the end of the string. It then adds the next vowel to the result array. If the character is not a vowel, it simply adds it to the result array. Finally, it joins the result array into a string and returns it.