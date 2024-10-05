```javascript
const countDistinctCharacters = (string) => {
  const set = new Set(string.toLowerCase().split(''));
  return set.size;
};
```

Explanation:
We use a Set to keep track of unique characters in the string. We convert the string to lowercase and split it into an array of characters using the `split` method. Then we iterate over the array and add each character to the Set. Sets in JavaScript automatically eliminate duplicate values, so we can use the size property of the Set to get the number of unique characters. 

The `toLowerCase` method is used to make the function case-insensitive, so it treats 'a' and 'A' as the same character. 

This function will return the number of distinct characters in the given string, regardless of case. For example, `countDistinctCharacters('xyzXYZ')` will return `3` and `countDistinctCharacters('Jerry')` will return `4`. 