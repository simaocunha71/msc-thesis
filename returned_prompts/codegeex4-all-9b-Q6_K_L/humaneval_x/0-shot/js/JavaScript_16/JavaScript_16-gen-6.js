Here's how you could write the function in JavaScript:

```javascript
const countDistinctCharacters = (string) => {
  let distinctCharacters = new Set(string.toLowerCase());
  return distinctCharacters.size;
};
```

In this function, we create a new Set to store unique characters from the string. We convert the string to lower case to ensure that characters are not considered distinct based on their case. Finally, we return the size of the set which is the count of unique characters in the string.