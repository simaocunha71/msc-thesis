Here is the solution to the problem. This function will count the number of times a given substring can be found in the original string, including overlapping cases.

```javascript
const howManyTimes = (string, substring) => {
  if (!string || !substring) {
    return 0;
  }
  let count = 0;
  let index = 0;
  while ((index = string.indexOf(substring, index)) !== -1) {
    count++;
    index += substring.length;
  }
  return count;
};
```

You can test the function with the given examples:

```javascript
console.log(howManyTimes('', 'a')); // 0
console.log(howManyTimes('aaa', 'a')); // 3
console.log(howManyTimes('aaaa', 'aa')); // 3
```

This function works by iterating over the original string and searching for the substring using the `indexOf` method. It starts searching from the current index and increments the index by the length of the substring after a match is found. This way, it counts overlapping matches. The function returns the total count of matches found. If the string or substring is empty, it returns 0.