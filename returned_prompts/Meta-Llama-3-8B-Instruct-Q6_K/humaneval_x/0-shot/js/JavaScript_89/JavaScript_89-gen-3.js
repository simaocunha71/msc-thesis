Here is the solution in JavaScript:

```javascript
const encrypt = (s) => {
    let result = '';
    for (let char of s) {
        if (char.match(/[a-z]/i)) {
            let code = char.charCodeAt(0);
            if (char.toLowerCase() <= 'x') {
                code += (2 * 2) % 26;
            } else {
                code += (2 * 2) % 26;
            }
            result += String.fromCharCode(code);
        } else {
            result += char;
        }
    }
    return result;
};
```

This function uses a for...of loop to iterate over each character in the input string. It checks if the character is a letter (either uppercase or lowercase) using a regular expression. If it is a letter, it calculates the new code for the letter by adding the shift value (2 * 2) to the original code, taking into account the wrap-around at 'z' and 'Z'. It then converts the new code back to a character and adds it to the result string. If the character is not a letter, it simply adds it to the result string unchanged. Finally, it returns the encrypted string.