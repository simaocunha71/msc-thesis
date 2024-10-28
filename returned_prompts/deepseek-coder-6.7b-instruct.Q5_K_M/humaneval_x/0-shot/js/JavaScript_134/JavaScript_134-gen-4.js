  return /[a-z]$/i.test(txt);

}

console.log(checkIfLastCharIsALetter("apple pie")); // ➞ false
console.log(checkIfLastCharIsALetter("apple pi e")); // ➞ true
console.log(checkIfLastCharIsALetter("apple pi e  ")); // ➞ false
console.log(checkIfLastCharIsALetter("")); // ➞ false

```



## ❓✏️✅Questions & Notes:

1. The `$` symbol in a Regular Expression (RegEx) is used to match the position right before the end of a string.

2. The `i` flag in the RegEx is used to make the search case insensitive. This means that the search will match both uppercase and lowercase letters.

3. The `test` method is a built-in method in JavaScript that tests for a match in a string. It returns `true` if it finds a match, and `false` if it does not.

4. The `console.log()` function is used to output the result of a function to the console. It can be used for testing purposes.

5. In JavaScript, `return` is used to specify the value to be returned by a function.

6. The RegEx `/[a-z]$/i` matches any character that is a lowercase or uppercase letter at the end of the string.

7. This function will return `true` if the last character of the input string is a letter (uppercase or lowercase), and `false` otherwise. If the string is empty, the function will return `false`.

## 🚀💻🧠Coding Challenge:

1. Create a function that takes a string as an argument and returns `true` if the first character of the string is a digit and `false` otherwise.

2. Create a function that takes a string as an argument and returns `true` if the string is a palindrome (reads the same backward as forward) and `false` otherwise.

3. Create a function that takes a string as an argument and returns the number of words