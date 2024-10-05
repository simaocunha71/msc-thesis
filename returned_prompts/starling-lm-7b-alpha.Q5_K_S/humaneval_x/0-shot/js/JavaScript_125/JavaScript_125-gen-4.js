To solve this kata, we can follow these steps:

1. Check if there are any whitespaces in the given string. If so, split the string on whitespaces and return the resulting array.
2. If there are no whitespaces in the string, check if there are any commas in the string. If so, split the string on commas and return the resulting array.
3. If there are no whitespaces or commas in the string, we need to count the number of lowercase letters with odd order in the alphabet. To do this, we can initialize a counter variable to 0 and iterate through each character in the string. For each character, we can check if it is a lowercase letter and if its Unicode code point minus 'a' (the Unicode code point of 'a') is odd. If both conditions are true, we increment the counter by 1. Finally, we return the counter as the result.

Here's the code that implements the above steps:

```javascript
const splitWords = (txt) => {
  // Step 1: Check for whitespaces
  if (txt.includes(' ')) {
    return txt.split(' ');
  } else if (txt.includes(',')) {
    // Step 2: Check for commas
    return txt.split(',');
  } else {
    // Step 3: Count odd-order lowercase letters
    let counter = 0;
    for (const char of txt) {
      if (char.match(/[a-z]/)) {
        const codePoint = char.charCodeAt(0);
        if ((codePoint - 'a' + 1) % 2 === 1) {
          counter++;
        }
      }
    }
    return counter;
  }
};
```

This function will correctly split the given string based on whitespaces or commas, or return the count of lowercase letters with odd order in the alphabet if no whitespaces or commas are found.

Explanation:
The provided solution uses conditional statements to determine the appropriate approach for splitting the given string. It first checks if the string contains whitespaces using the `includes` method. If it does, the string is split on whitespaces using the `split` method and the