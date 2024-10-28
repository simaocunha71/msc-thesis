```javascript
const longest = (strings) => {
  if (!strings.length) return null; // Return null if the input list is empty
  let longestStr = strings[0]; // Initialize the longest string as the first one
  for (let str of strings) {
    if (str.length > longestStr.length) longestStr = str; // Update the longest string if a longer one is found
  }
  return longestStr; // Return the longest string
};
```


Explanation:
The function `longest` takes a list of strings as input and returns the longest one. If the input list is empty, it returns `null`. It initializes the longest string as the first one in the list. Then, it iterates over the list, checking if each string is longer than the current longest string. If it is, it updates the longest string. Finally, it returns the longest string. If multiple strings have the same length, it returns the first one it encounters.