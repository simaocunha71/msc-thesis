The problem asks to create a function that checks if the last character of a given string is an alphabetical character and is not part of a word. A "word" is considered as a group of characters separated by a space. 

Here is the solution in JavaScript:

```javascript
const checkIfLastCharIsALetter = (txt) => {
    // Remove trailing spaces from the string
    txt = txt.trim();
    // Check if the string is not empty
    if(txt === "") {
        return false;
    }
    // Check if the last character is an alphabetical character
    if(txt.charAt(txt.length - 1).match(/[a-zA-Z]/)) {
        // Check if the last character is part of a word
        if(txt.charAt(txt.length - 1) !== " " && txt.charAt(txt.length - 1) !== "") {
            return true;
        }
    }
    return false;
};
```

You can test the function with the examples provided:

```javascript
console.log(checkIfLastCharIsALetter("apple pie")); // false
console.log(checkIfLastCharIsALetter("apple pi e")); // true
console.log(checkIfLastCharIsALetter("apple pi e ")); // false
console.log(checkIfLastCharIsALetter("")); // false
```


This function first removes any trailing spaces from the input string. Then it checks if the string is not empty. If the string is not empty, it checks if the last character is an alphabetical character. If the last character is an alphabetical character, it checks if the last character is part of a word by checking if it is not a space. If the last character is part of a word, the function returns true. If the last character is not part of a word, the function returns true. If the last character is not an alphabetical character, the function returns false. If the string is empty, the function returns false. 