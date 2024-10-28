Here is the solution to the problem:

```javascript
const longest = (strings) => {
  if (strings.length === 0) {
    return null;
  }
  let longestString = strings[0];
  for (let i = 1; i < strings.length; i++) {
    if (strings[i].length > longestString.length) {
      longestString = strings[i];
    } else if (strings[i].length === longestString.length) {
      longestString = strings[i];
      break;
    }
  }
  return longestString;
};
```


This function takes an array of strings as input and returns the longest one. If the input array is empty, it returns null. It iterates over the array of strings and keeps track of the longest string it has seen so far. If it finds a string that is longer than the current longest string, it updates the longest string. If it finds a string that is the same length as the current longest string, it updates the longest string and breaks out of the loop. Finally, it returns the longest string.