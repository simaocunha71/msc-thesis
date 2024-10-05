To solve this Kata, we can follow the following steps:

1. Check if the string contains whitespace characters or commas. If it does, we can split the string using the whitespace or comma delimiter. This can be done using the split() function in JavaScript. For example, if the string is "Hello world!", we can use split(' ') or split(',') to split the string into an array of words.

2. If the string does not contain any whitespace characters or commas, we can count the number of lower-case letters with odd order in the alphabet. We can achieve this by iterating over each character in the string and checking if it is a lower-case letter. If it is, we can use the ord() function to get the Unicode value of the character and check if it is odd. If it is, we increment a counter variable.

3. Finally, we can return the result of the split operation or the count of odd-order lower-case letters, depending on the condition in step 1.

Here's an example implementation of the splitWords function in JavaScript:

```javascript
const splitWords = (txt) => {
  if (txt.includes(' ') || txt.includes(',')) {
    return txt.split(/[ ,]+/);
  } else {
    const count = txt.replace(/[^a-z]/g, '').split('').filter(c => c.charCodeAt(0) % 2 === 1).length;
    return count;
  }
};
```

This implementation first checks if the string contains whitespace or comma characters using the includes() method. If it does, it splits the string using the split() method and returns the resulting array. If it does not contain any whitespace or comma characters, it replaces all non-alphabetic characters with an empty string using the replace() method, splits the resulting string into an array of characters using the split() method, and then filters out the characters that are not lower-case letters using the filter() method. Finally, it counts the number of odd-order lower-case letters in the filtered array and returns the count.

This implementation should pass the provided test cases and return the expected results.

*/

//code

```
```