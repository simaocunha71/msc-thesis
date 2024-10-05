You can solve this problem by using a Set data structure. A Set automatically removes duplicates from a collection of values. By converting the input string to lowercase and then into a Set, you can count the number of distinct characters.

Here is a JavaScript solution:

```javascript
const countDistinctCharacters = (string) => {
  const lowerCaseString = string.toLowerCase();
  const distinctCharacters = new Set(lowerCaseString);
  return distinctCharacters.size;
}
```

You can test this function with your examples:

```javascript
console.log(countDistinctCharacters('xyzXYZ')); // 3
console.log(countDistinctCharacters('Jerry')); // 4
```

This function will return the number of distinct characters in the string, regardless of case. For example, 'xyzXYZ' has 3 distinct characters: 'x', 'y', and 'z'. 'Jerry' has 4 distinct characters: 'j', 'e', 'r', and 'y'.