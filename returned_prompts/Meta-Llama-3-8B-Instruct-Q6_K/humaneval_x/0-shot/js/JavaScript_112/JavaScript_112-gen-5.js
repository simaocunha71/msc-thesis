```javascript
const reverseDelete = (s, c) => {
    let res = s.split('').filter(x => !c.includes(x)).join('');
    return [res, res === res.split('').reverse().join('')];
}
```


Explanation:
1. First, we split the string `s` into an array of individual characters using `split('')`.
2. Then, we use the `filter()` method to create a new array with only the characters that are not in the string `c`. We use the callback function `x => !c.includes(x)` to check if a character is not in `c`.
3. We join the filtered array back into a string using `join('')`.
4. Then, we check if the resulting string is a palindrome by comparing it with its reverse using `res === res.split('').reverse().join('')`.
5. Finally, we return a tuple containing the result string and a boolean value indicating whether it is a palindrome. We use an array `[res, res === res.split('').reverse().join('')]` to return both values.