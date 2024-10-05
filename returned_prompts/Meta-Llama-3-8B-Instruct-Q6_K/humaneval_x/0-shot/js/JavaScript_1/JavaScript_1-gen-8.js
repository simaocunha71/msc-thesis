Here is a JavaScript solution for your problem:

```javascript
const separateParenGroups = (paren_string) => {
    let result = [];
    let currentGroup = '';
    let openCount = 0;

    for (let i = 0; i < paren_string.length; i++) {
        if (paren_string[i] === '(') {
            openCount++;
            currentGroup += paren_string[i];
        } else if (paren_string[i] === ')') {
            openCount--;
            currentGroup += paren_string[i];
            if (openCount === 0) {
                result.push(currentGroup);
                currentGroup = '';
            }
        }
    }

    return result;
}

console.log(separateParenGroups('( ) (( )) (( )( ))'));
// Output: ['()', '(())', '(()())']
```

This function works by iterating over the input string. It keeps track of the current group of parentheses and the count of open parentheses. When it encounters a closing parenthesis, it decreases the open count. When the open count becomes zero, it means a group of parentheses has been completed, so it adds the current group to the result array and resets the current group. Finally, it returns the result array.