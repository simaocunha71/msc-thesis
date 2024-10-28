```javascript
const countDistinctCharacters = (string) => {
  let charSet = new Set();
  for (let char of string.toLowerCase()) {
    charSet.add(char);
  }
  return charSet.size;
};

console.log(countDistinctCharacters('xyzXYZ')); // 3
console.log(countDistinctCharacters('Jerry')); // 4
````
Explanation:
The function `countDistinctCharacters` takes a string as an argument and returns the number of distinct characters in the string. It uses a Set to keep track of the unique characters in the string. The Set is a collection of unique elements, so it automatically removes any duplicate characters.

The function converts the input string to lowercase using the `toLowerCase()` method, so that the count is case-insensitive. It then iterates over each character in the string using a `for...of` loop, and adds each character to the Set.

Finally, the function returns the size of the Set, which represents the number of distinct characters in the string.

In the example code, we call the `countDistinctCharacters` function with two strings, 'xyzXYZ' and 'Jerry', and log the results to the console. The output is `3` and `4`, respectively, which are the correct counts of distinct characters in each string.