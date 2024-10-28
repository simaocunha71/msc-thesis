
```js
const splitWords = (txt) => {
    if (txt.includes(' ')) {
        return txt.split(' ');
    } else if (txt.includes(',')) {
        return txt.split(',');
    } else {
        let count = 0;
        for (let i = 0; i < txt.length; i++) {
            if (txt[i] === txt[i].toLowerCase() && txt.charCodeAt(i) % 2 !== 0) {
                count++;
            }
        }
        return count;
    }
};

console.log(splitWords("Hello world!")) // ➞  ["Hello", "world!"]
console.log(splitWords("Hello,world!")) // ➞  ["Hello", "world!"]
console.log(splitWords("abcdef")) // 3
```

This function works by checking if the input string contains a space or a comma. If it does, it splits the string at that character into an array. If it doesn't contain either, it counts the number of lowercase letters with odd ASCII values (i.e. their ASCII value is odd) and returns that count.

Please note that the problem statement is a bit ambiguous. It says to return the number of lower-case letters with odd order in the alphabet, but also states that the ASCII value of a character is odd if the character is a lower-case letter. In this case, the function is counting the number of lower-case letters in the string that have an ASCII value that is odd. If this interpretation is incorrect, please clarify.

This function is case-sensitive, meaning it will not count upper-case letters as lower-case. If you want to count upper-case letters as well, you can modify the function to check if the ASCII value of a character is odd by comparing it to the ASCII values of lower-case letters 'a' through 'z'.

If you want to ignore upper-case letters, you can add a condition to check if the character is upper-case and skip it if it is.

If you want to count upper-case letters with odd ASCII values, you can modify the function to check if the ASC