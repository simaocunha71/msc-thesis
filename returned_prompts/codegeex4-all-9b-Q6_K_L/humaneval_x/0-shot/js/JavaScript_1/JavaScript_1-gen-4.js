```javascript
const separateParenGroups = (paren_string) => {
    const groups = [];
    let currentGroup = '';
    let depth = 0;

    for (const c of paren_string) {
        if (c === '(') {
            depth++;
            currentGroup += c;
        } else if (c === ')') {
            depth--;
            currentGroup += c;
            if (depth === 0) {
                groups.push(currentGroup);
                currentGroup = '';
            }
        }
    }

    return groups;
}
```
