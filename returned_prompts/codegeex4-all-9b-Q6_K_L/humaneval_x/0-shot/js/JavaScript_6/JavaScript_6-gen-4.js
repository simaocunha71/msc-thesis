```js
const parseNestedParens = (paren_string) => {
    var groups = paren_string.split(' ');
    var results = [];

    for (let i = 0; i < groups.length; i++) {
        var maxDepth = 0;
        var currentDepth = 0;
        var group = groups[i];

        for (let j = 0; j < group.length; j++) {
            if (group[j] === '(') {
                currentDepth += 1;
                if (currentDepth > maxDepth) {
                    maxDepth = currentDepth;
                }
            } else if (group[j] === ')') {
                currentDepth -= 1;
            }
        }
        results.push(maxDepth);
    }

    return results;
}
```