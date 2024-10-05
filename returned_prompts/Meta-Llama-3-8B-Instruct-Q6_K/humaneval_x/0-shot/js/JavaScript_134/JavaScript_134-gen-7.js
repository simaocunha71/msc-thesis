Here is a JavaScript solution for the problem:

```javascript
const checkIfLastCharIsALetter = (txt) => {
    // Remove trailing spaces
    txt = txt.trim();
    // Check if the string is not empty
    if (txt.length === 0) {
        return false;
    }
    // Check if the last character is a letter
    if (!/[a-zA-Z]/.test(txt.charAt(txt.length - 1))) {
        return false;
    }
    // Check if the last character is part of a word
    if (/[a-zA-Z]/.test(txt.charAt(txt.length - 2))) {
        return true;
    }
    return false;
};
```

The function `checkIfLastCharIsALetter` takes a string `txt` as an argument. It first removes any trailing spaces from the string using the `trim` method. Then it checks if the string is not empty. If it is empty, it returns `false`.

Next, it checks if the last character of the string is a letter using a regular expression. If it is not a letter, it returns `false`.

Finally, it checks if the last character is part of a word by checking if the character before it is a letter. If it is, it returns `true`. If none of the above conditions are met, it returns `false`.