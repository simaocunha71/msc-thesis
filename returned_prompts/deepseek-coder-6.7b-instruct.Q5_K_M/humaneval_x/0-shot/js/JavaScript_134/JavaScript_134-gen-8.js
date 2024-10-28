  return /[a-z]$/i.test(txt);

};
console.log(checkIfLastCharIsALetter("apple pie")); // false
console.log(checkIfLastCharIsALetter("apple pi e")); // true
console.log(checkIfLastCharIsALetter("apple pi e  ")); // false
console.log(checkIfLastCharIsALetter("")); // false

// The regular expression /[a-z]$/i checks if the last character is a letter (either lower case or upper case due to the 'i')
// The .test() function is used to test for a match in the string.
// If it finds a match, it returns true, otherwise it returns false.

```



## Answer 2

```javascript
function checkIfLastCharIsALetter(txt) {
    return /[a-z]$/i.test(txt);
}

console.log(checkIfLastCharIsALetter("apple pie")); // false
console.log(checkIfLastCharIsALetter("apple pi e")); // true
console.log(checkIfLastCharIsALetter("apple pi e  ")); // false
console.log(checkIfLastCharIsALetter("")); // false
```



## Answer 3

```javascript
function checkIfLastCharIsALetter(txt) {
    return /[a-z]$/i.test(txt);
}

console.log(checkIfLastCharIsALetter("apple pie")); // false
console.log(checkIfLastCharIsALetter("apple pi e")); // true
console.log(checkIfLastCharIsALetter("apple pi e  ")); // false
console.log(checkIfLastCharIsALetter("")); // false
```



## Answer 4

```javascript
function checkIfLastCharIsALetter(txt) {
    return /[a-z]$/i.test(txt);
}

console.log(checkIfLastCharIsALetter("apple pie")); // false
console.log(checkIfLastCharIsALetter("apple pi e")); // true
