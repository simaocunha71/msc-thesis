```javascript
const histogram = (test) => {
  const dict = {};
  const words = test.split(' ');
  let maxCount = 0;
  let maxLetter = '';
  for (let word of words) {
    if (dict[word]) {
      dict[word] += 1;
    } else {
      dict[word] = 1;
    }
    if (dict[word] > maxCount) {
      maxCount = dict[word];
      maxLetter = word;
    }
  }
  if (maxCount === 0) {
    return {};
  } else {
    let result = {};
    for (let letter in dict) {
      if (dict[letter] === maxCount) {
        result[letter] = maxCount;
      }
    }
    return result;
  }
}
```

This solution works by first splitting the input string into an array of words. Then it creates a dictionary to store the count of each letter. It loops through the array of words and updates the count in the dictionary. It also keeps track of the maximum count and the corresponding letter. Finally, it creates a new dictionary to store the letters with the maximum count and returns it. If the maximum count is 0, it returns an empty dictionary.