```javascript
const countDistinctCharacters = (string) => {
  // Convert the string to lowercase to ignore case
  string = string.toLowerCase();
  // Initialize a Set to store unique characters
  const uniqueChars = new Set();
  // Iterate over the string
  for (let char of string) {
    // Add each character to the Set
    uniqueChars.add(char);
  }
  // Return the size of the Set, which represents the number of distinct characters
  return uniqueChars.size;
};
```
This function uses a Set to store unique characters from the input string. A Set is a data structure that stores unique values, so it's perfect for this task. We convert the input string to lowercase to ignore case. Then, we iterate over the string and add each character to the Set. Finally, we return the size of the Set, which represents the number of distinct characters. This approach has a time complexity of O(n), where n is the length of the input string.