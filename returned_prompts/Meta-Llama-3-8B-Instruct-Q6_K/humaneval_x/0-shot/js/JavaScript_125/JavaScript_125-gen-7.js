```javascript
const splitWords = (txt) => {
  if (/^\s*$/.test(txt)) return [];
  if (/\s+/.test(txt)) return txt.split(/\s+/);
  if (/\,/.test(txt)) return txt.split(',');
  return txt.toLowerCase().split('').filter((c, i) => ord(c) % 2 !== 0).length;
};

const ord = (c) => c.charCodeAt(0) - 97;
```


Explanation:

The function `splitWords` takes a string as an argument. It first checks if the string contains only whitespace characters. If it does, it returns an empty array.

Next, it checks if the string contains any whitespace characters. If it does, it splits the string into an array of words using the `split` method with a regular expression that matches one or more whitespace characters.

If the string does not contain any whitespace characters, it checks if it contains any commas. If it does, it splits the string into an array of words using the `split` method with a regular expression that matches commas.

If the string does not contain any whitespace or commas, it converts the string to lowercase and splits it into an array of characters. It then filters this array to keep only the characters that are in odd positions (i.e., the characters at indices 1, 3, 5, etc.). The length of this filtered array is returned as the result.

The `ord` function is used to convert a character to its corresponding integer value in the alphabet (where 'a' is 0, 'b' is 1, etc.). It does this by subtracting 97 from the character code of the character (which gives the position of the character in the alphabet). This function is used in the `splitWords` function to determine whether a character is in an odd position in the alphabet.