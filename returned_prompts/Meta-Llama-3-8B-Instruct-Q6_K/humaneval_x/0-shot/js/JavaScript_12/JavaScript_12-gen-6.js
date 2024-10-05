```
const longest = (strings) => {
  if (!strings.length) return null; // If the list is empty, return null
  let longestStr = strings[0]; // Initialize the longest string with the first string in the list
  for (let str of strings) {
    if (str.length > longestStr.length) {
      longestStr = str; // Update the longest string if a longer one is found
    }
  }
  return longestStr;
};
```


This function works by first checking if the input list is empty. If it is, it returns null. Otherwise, it initializes the longest string with the first string in the list. Then, it iterates over the rest of the strings in the list, updating the longest string if a longer one is found. Finally, it returns the longest string found.

Note that the function returns the first string in case of multiple strings of the same length, as per the problem statement. If you want to return all strings of the maximum length, you would need to modify the function accordingly.