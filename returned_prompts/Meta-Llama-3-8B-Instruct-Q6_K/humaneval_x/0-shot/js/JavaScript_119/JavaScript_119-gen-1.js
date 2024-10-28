You can solve this problem by counting the number of open and close parentheses in each string. If the total number of open parentheses in both strings is equal to the total number of close parentheses, then it is possible to concatenate them in some order to form a good string.

Here is the implementation in JavaScript:

```javascript
const matchParens = (lst) => {
    const open = lst[0].split('').filter(c => c === '(').length;
    const close = lst[0].split('').filter(c => c === ')').length;
    if (open > close) {
        return 'No';
    }
    if (open < close) {
        return 'No';
    }
    open = lst[1].split('').filter(c => c === '(').length;
    close = lst[1].split('').filter(c => c === ')').length;
    if (open > close) {
        return 'No';
    }
    if (open < close) {
        return 'Yes';
    }
    return 'Yes';
};
```

This function first calculates the number of open and close parentheses in the first string. If the number of open parentheses is greater than the number of close parentheses, or if the number of close parentheses is greater than the number of open parentheses, then it returns 'No'. If the numbers are equal, then it calculates the number of open and close parentheses in the second string. If the number of open parentheses in the second string is greater than the number of close parentheses, then it returns 'No'. If the numbers are equal, then it returns 'Yes'. If the number of close parentheses in the second string is greater than the number of open parentheses, then it returns 'Yes'. This is because we can always match the extra close parentheses with the open parentheses in the first string.