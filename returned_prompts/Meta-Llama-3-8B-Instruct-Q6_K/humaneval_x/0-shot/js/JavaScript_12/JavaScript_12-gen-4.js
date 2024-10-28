```javascript
const longest = (strings) => {
  if (strings.length === 0) return null;
  let longestStr = strings[0];
  for (let str of strings) {
    if (str.length > longestStr.length) {
      longestStr = str;
    }
  }
  return longestStr;
};
```



The function `longest` takes a list of strings as an argument and returns the longest one. If the input list is empty, it returns `null`. If there are multiple strings of the same length, it returns the first one. The function iterates over the list of strings and keeps track of the longest string found so far. If a string with a longer length is found, it updates the `longestStr` variable. Finally, it returns the longest string found.