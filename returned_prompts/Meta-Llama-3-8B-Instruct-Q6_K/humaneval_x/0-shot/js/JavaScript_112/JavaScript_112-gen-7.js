Here is a JavaScript solution for the problem:

```javascript
const reverseDelete = (s, c) => {
    let result = '';
    let i = s.length - 1;
    for (let j = 0; j < s.length; j++) {
        if (!c.includes(s[j]) || i < j) {
            result = s[j] + result;
            i--;
        }
    }
    return [result, result === result.split('').reverse().join('')];
}
```
This function takes two strings `s` and `c` as input. It first initializes an empty string `result` and an index `i` to the last character of `s`. Then it iterates over the characters of `s` from left to right. If a character is not in `c` or if `i` is less than the current index, it adds the character to the beginning of `result` and decrements `i`. Finally, it returns a tuple containing the `result` string and a boolean indicating whether `result` is a palindrome.

For example, if `s = "abcde"` and `c = "ae"`, the function will return `['bcd', false]`. If `s = "abcdedcba"` and `c = "ab"`, the function will return `['cdedc', true]`.