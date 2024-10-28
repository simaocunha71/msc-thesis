```javascript
const countDistinctCharacters = (string) => {
  // Convert the string to lowercase to ignore case sensitivity
  const lowerCaseString = string.toLowerCase();

  // Create an empty Set to store unique characters
  const uniqueCharacters = new Set();

  // Iterate over each character in the string
  for (let i = 0; i < lowerCaseString.length; i++) {
    // Add the character to the Set
    uniqueCharacters.add(lowerCaseString[i]);
  }

  // Return the number of unique characters
  return uniqueCharacters.size;
}
```