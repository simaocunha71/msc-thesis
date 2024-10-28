Here is the solution in JavaScript:

```javascript
const histogram = (test) => {
  if (!test) return {};

  let letterCount = {};
  let maxCount = 0;

  for (let letter of test.split(' ')) {
    if (letterCount[letter]) {
      letterCount[letter]++;
    } else {
      letterCount[letter] = 1;
    }

    if (letterCount[letter] > maxCount) {
      maxCount = letterCount[letter];
    }
  }

  let result = {};

  for (let letter in letterCount) {
    if (letterCount[letter] === maxCount) {
      result[letter] = letterCount[letter];
    }
  }

  return result;
};
```
This function first splits the input string into individual letters. Then it counts the occurrence of each letter and keeps track of the maximum count. Finally, it creates a dictionary of the letters with the maximum count and returns it. If there are multiple letters with the same maximum count, it will include all of them in the result. If the input string is empty, it will return an empty dictionary. 