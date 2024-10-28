```javascript
const howManyTimes = (string, substring) => {
  if (!string || !substring) {
    return 0;
  }
  let count = 0;
  let index = 0;
  while (index < string.length) {
    index = string.indexOf(substring, index);
    if (index === -1) {
      break;
    }
    count++;
    index += substring.length;
  }
  return count;
};
```


This function uses the `indexOf` method to find the index of the first occurrence of the substring in the string. It then increments the count and moves the index forward by the length of the substring. This process is repeated until no more occurrences of the substring are found. The function returns the count of occurrences. If the input strings are empty, the function returns 0.