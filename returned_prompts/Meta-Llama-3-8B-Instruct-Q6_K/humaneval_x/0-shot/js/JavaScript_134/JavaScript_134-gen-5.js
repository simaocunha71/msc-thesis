Here is a JavaScript solution for the problem:

```javascript
const checkIfLastCharIsALetter = (txt) => {
  // Remove leading and trailing spaces
  txt = txt.trim();
  
  // Check if the string is empty
  if (txt === '') {
    return false;
  }
  
  // Get the last character of the string
  let lastChar = txt.charAt(txt.length - 1);
  
  // Check if the last character is an alphabetical character
  if (!/^[a-zA-Z]$/.test(lastChar)) {
    return false;
  }
  
  // Check if the last character is part of a word
  if (/\s/.test(txt.substring(0, txt.length - 1))) {
    return false;
  }
  
  return true;
};
```

This function first trims the input string to remove leading and trailing spaces. Then it checks if the string is empty. If it is, the function returns false. 

Then it gets the last character of the string using the `charAt` method. It checks if the last character is an alphabetical character using a regular expression. If it's not, the function returns false.

Finally, it checks if the last character is part of a word by checking if there's a space before it. If there is, the function returns false. If none of the checks fail, the function returns true. 

You can test this function with the examples provided in the problem statement to see that it produces the expected output.