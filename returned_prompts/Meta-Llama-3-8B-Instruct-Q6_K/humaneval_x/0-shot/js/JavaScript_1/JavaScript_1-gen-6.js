```
function separateParenGroups(paren_string) {
    let groups = [];
    let currentGroup = '';
    let depth = 0;

    for (let char of paren_string) {
        if (char === '(') {
            depth++;
            currentGroup += char;
        } else if (char === ')') {
            depth--;
            currentGroup += char;
            if (depth === 0) {
                groups.push(currentGroup);
                currentGroup = '';
            }
        }
    }

    return groups;
}

console.log(separateParenGroups('( ) (( )) (( )( ))'));
// Output: ["()", "(())", "(()())"]
```


The function separateParenGroups() takes a string of parentheses as an input, and returns a list of separate groups of balanced parentheses. It iterates over the input string, using a counter depth to keep track of the current nesting level. When it encounters a '(', it increments the depth, and when it encounters a ')', it decrements the depth. When the depth becomes zero, it means a group has been closed, and it adds the current group to the list of groups and resets the current group. Finally, it returns the list of groups. The function is implemented in a way that it ignores any spaces in the input string.