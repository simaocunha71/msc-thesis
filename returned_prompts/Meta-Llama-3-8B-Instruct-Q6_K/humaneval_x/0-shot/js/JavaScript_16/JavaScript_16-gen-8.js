```javascript
const countDistinctCharacters = (string) => {
  const charSet = new Set();
  for (let char of string.toLowerCase()) {
    charSet.add(char);
  }
  return charSet.size;
};
```
Explanation:
The task is to count the number of distinct characters in a given string, regardless of case. To achieve this, we use a Set in JavaScript, which is a collection of unique values. 

First, we create a new Set named `charSet`. Then, we iterate over each character in the input string, converting it to lowercase to ensure case-insensitivity. We add each character to the `charSet`. Finally, we return the size of the `charSet`, which represents the number of distinct characters in the input string. 

The `toLowerCase()` method is used to convert each character to lowercase before adding it to the `charSet`, so that characters like 'a' and 'A' are considered the same. This ensures that the count of distinct characters is case-insensitive. 

The `Set` data structure automatically removes duplicate values, so we don't need to worry about handling duplicate characters. The `size` property of the `Set` returns the number of unique elements in the set, which is the desired output. 

The `countDistinctCharacters` function can be tested with the given examples to verify its correctness. 

Example:
```javascript
console.log(countDistinctCharacters('xyzXYZ')); // Output: 3
console.log(countDistinctCharacters('Jerry')); // Output: 4
```  ```javascript
const countDistinctCharacters = (string) => {
  const charSet = new Set();
  for (let char of string.toLowerCase()) {
    charSet.add(char);
  }
  return charSet.size;
};

console.log(countDistinctCharacters('xyzXYZ')); // Output: 3
console.log(countDistinctCharacters('Jerry')); // Output: 4
```
This code defines the `countDistinctCharacters` function, which takes a string as input and returns the number of distinct characters in the string, ignoring case. The function uses a Set to keep track of unique characters, and the `size` property of the Set is used to return the count of distinct characters.

The code then logs the results of calling the `countDistinctCharacters` function with the examples 'xyzXYZ' and 'Jerry'. The output is:
```
3
4
```
This shows that the function correctly counts the number of distinct characters in each string, ignoring case.