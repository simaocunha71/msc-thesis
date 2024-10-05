```
const splitWords = (txt) => {
  // split on whitespace
  const words = txt.split(/\s+/);
  
  // if no whitespace, split on commas
  if (!words[0]) {
    words = txt.split(',');
  }
  
  // if still no split, count odd alphabet letters
  if (!words.length) {
    let count = 0;
    for (let char of txt.toLowerCase()) {
      if (char.match(/[a-z]/) && ord(char) % 2 !== 0) {
        count++;
      }
    }
    return count;
  }
  
  return words;
};
```



Here's a breakdown of the solution:

1. We first split the input string on whitespace using the `split()` method with a regular expression that matches one or more whitespace characters (`/\s+/`).
2. If the resulting array is empty, it means there were no whitespace characters in the input string, so we split on commas instead.
3. If the resulting array is still empty, it means there were no commas in the input string either. In this case, we count the number of lower-case letters with odd order in the alphabet. We do this by iterating over the characters in the input string (converted to lower-case), checking if each character is a letter (using the `match()` method with a regular expression), and if it's an odd-numbered letter (using the `ord()` function and the modulo operator `% 2 !== 0`). We increment a counter for each letter that meets these conditions.
4. Finally, if the input string was split on whitespace or commas, we return the resulting array of words. If the input string was split on odd alphabet letters, we return the count of such letters.

The `ord()` function is not a built-in JavaScript function, so we would need to define it separately. Here's a simple implementation:
```
function ord(char) {
  return char.charCodeAt(0) - 97;
}
```
This function takes a character as input and returns its ASCII code value minus 97, which gives us the position of the character in the alphabet (with 'a' being 0 and 'z' being 25).