```javascript
const longest = (strings) => {
  if (!strings.length) return null; // if the list is empty, return null
  let longestStr = strings[0]; // initialize the longest string as the first string in the list
  for (let str of strings) {
    if (str.length > longestStr.length) {
      longestStr = str; // update the longest string if a longer one is found
    }
  }
  return longestStr;
};
