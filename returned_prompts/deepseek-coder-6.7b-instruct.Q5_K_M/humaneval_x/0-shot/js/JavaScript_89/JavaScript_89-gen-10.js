let result = '';
    for(let i = 0; i < s.length; i++) {
        let code = s.charCodeAt(i);
        if (code >= 65 && code <= 90) {
            result += String.fromCharCode(65 + ((code - 65 + 2*2) % 26));
        } else if (code >= 97 && code <= 122) {
            result += String.fromCharCode(97 + ((code - 97 + 2*2) % 26));
        } else {
            result += s.charAt(i);
        }
    }
    return result;
}

console.log(encrypt('hi')); // lm
console.log(encrypt('asdfghjkl')); // ewhjklnop
console.log(encrypt('gf')); // kj
console.log(encrypt('et')); // ix


The function works by looping through the string. For each character, it gets the ASCII code and checks if it's a uppercase or lowercase letter by comparing it to the ASCII values of 'A' and 'a'. If it is a letter, it adds 2 (for the rotation) to the ASCII value, then applies the modulo 26 operation to wrap it around the alphabet. Finally, it converts this new code back to a character using String.fromCharCode and adds it to the result string. If the character is not a letter, it just adds it to the result string as is.































































































































































