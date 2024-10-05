Here is a solution written in JavaScript:

```javascript
const separateParenGroups = (paren_string) => {
    const groups = [];
    let currentGroup = "";
    let openBraces = 0;

    for (let i = 0; i < paren_string.length; i++) {
        if (paren_string[i] === "(") {
            if (openBraces === 0) {
                currentGroup = "(";
            }
            openBraces++;
        } else if (paren_string[i] === ")") {
            openBraces--;
            if (openBraces === 0) {
                currentGroup += ")";
                groups.push(currentGroup);
                currentGroup = "";
            } else {
                currentGroup += paren_string[i];
            }
        }
    }

    return groups;
}
```

In this solution, we iterate over each character in the input string. If we encounter an opening brace, we increase the count of open braces. If the count is zero, we start a new group. If we encounter a closing brace, we decrease the count of open braces. If the count is zero, we have reached the end of a group, so we add the group to the list of groups and start a new group. If the count is not zero, we add the closing brace to the current group. Finally, we return the list of groups.