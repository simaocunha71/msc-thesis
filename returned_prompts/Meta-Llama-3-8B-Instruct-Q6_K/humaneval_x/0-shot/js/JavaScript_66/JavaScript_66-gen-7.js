Here is a JavaScript solution for the problem:

```javascript
const digitSum = (s) => {
    let sum = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i].toUpperCase() === s[i]) {
            sum += s.charCodeAt(i);
        }
    }
    return sum;
};
```

This function iterates through each character in the input string. If the character is uppercase (checked using `s[i].toUpperCase() === s[i]`), it adds the character's ASCII code (obtained using `s.charCodeAt(i)`) to the sum. The function then returns the total sum. 

This solution works because the `charCodeAt` method returns the Unicode code point for the character at the specified index in the string. For uppercase letters, these code points range from 65 (for 'A') to 90 (for 'Z'). The `toUpperCase` method is used to check if a character is uppercase, as it returns the uppercase equivalent of the character if it is lowercase, and the original character if it is uppercase. 

For example, `s[0].toUpperCase() === s[0]` would be `true` for the first character 'A' (both 'A' and 'a' are uppercase), but `false` for the first character 'a' (only 'A' is uppercase). 

This solution assumes that the input string only contains ASCII characters. If the string may contain non-ASCII characters, a more complex solution would be needed. 

The time complexity of this solution is O(n), where n is the length of the input string, as it needs to iterate through each character in the string. The space complexity is O(1), as it only uses a constant amount of space to store the sum. 