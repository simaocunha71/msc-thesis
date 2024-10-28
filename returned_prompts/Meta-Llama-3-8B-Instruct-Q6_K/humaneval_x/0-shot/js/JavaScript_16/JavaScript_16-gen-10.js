```javascript
function countDistinctCharacters(str) {
  const charSet = new Set(str.toLowerCase().split(''));
  return charSet.size;
}

console.log(countDistinctCharacters('xyzXYZ')); // 3
console.log(countDistinctCharacters('Jerry')); // 4
```
Explanation:
The problem is asking to count the number of distinct characters in a given string, ignoring the case of the characters. 

To solve this, we can convert the string to lower case and split it into an array of characters. Then, we can use a Set to keep track of unique characters. A Set in JavaScript is a collection of unique values, so by converting the array of characters to a Set, we automatically get rid of any duplicate characters. Finally, we can return the size of the Set, which represents the number of distinct characters in the string.

In the code above, we define a function `countDistinctCharacters` that takes a string as input. We convert the string to lower case using the `toLowerCase()` method, split it into an array of characters using the `split('')` method, and then convert the array to a Set using the `Set` constructor. Finally, we return the size of the Set using the `size` property. 

We test this function with the examples given in the problem statement, and it returns the expected results.