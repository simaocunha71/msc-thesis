Here is the solution in JavaScript:

```javascript
const longest = (strings) => {
  if (strings.length === 0) {
    return null;
  }

  let longestString = strings[0];
  for (let i = 1; i < strings.length; i++) {
    if (strings[i].length > longestString.length) {
      longestString = strings[i];
    }
  }

  return longestString;
}
```
This function iterates over all the strings in the input list and keeps track of the longest one. If the input list is empty, it returns null.