To check if two words have the same characters, we can follow these steps:

1. Create an empty object to store the frequency of each character in the first word.
2. Iterate through the first word and for each character, increment its count in the object.
3. Iterate through the second word and for each character:
   - If the character is present in the object, decrement its count. If the count becomes 0, remove the character from the object.
   - If the character is not present in the object, return false.
4. If we reach the end of the second word and the object is empty, return true. Otherwise, return false.

Here's the code that implements the above steps:

```javascript
const sameChars = (s0, s1) => {
  const charFreq = {};

  // Step 1: Create an empty object to store the frequency of each character in the first word
  for (const char of s0) {
    charFreq[char] = (charFreq[char] || 0) + 1;
  }

  // Step 2: Iterate through the first word and for each character, increment its count in the object

  // Step 3: Iterate through the second word and for each character
  for (const char of s1) {
    if (!charFreq[char]) {
      // If the character is not present in the object, return false
      return false;
    } else {
      // If the character is present in the object, decrement its count
      charFreq[char]--;
      if (charFreq[char] === 0) {
        delete charFreq[char];
      }
    }
  }

  // Step 4: If we reach the end of the second word and the object is empty, return true. Otherwise, return false
  return Object.keys(charFreq).length === 0;
};
```

You can use the `sameChars` function to check if two words have the same characters. It will return `true` if the characters are the same, and `false` otherwise.

Here are some examples of how to use the `sameChars` function:

```javascript
console.