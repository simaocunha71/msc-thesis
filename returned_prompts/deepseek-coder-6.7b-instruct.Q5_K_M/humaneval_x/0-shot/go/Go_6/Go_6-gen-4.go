    paren_strings := strings.Split(paren_string, " ")
    depths := make([]int, len(paren_strings))

B:
    for idx, group := range paren_strings {
        maxDepth := 0
        currentDepth := 0

C:
        for _, char := range group {
            if string(char) == "(" {
                currentDepth += 1
                maxDepth = int(math.Max(float64(maxDepth), float64(currentDepth)))
            } else if string(char) == ")" {
                currentDepth -= 1
            }
        }

D:
        depths[idx] = maxDepth
    }

E:
    return depths
}
```

## Python Solution:

```python
import re

def parse_nested_parens(paren_string):
    groups = re.split('\s+', paren_string)
    depths = []

    for group in groups:
        max_depth = 0
        current_depth = 0

        for char in group:
            if char == '(':
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
            elif char == ')':
                current_depth -= 1

        depths.append(max_depth)

    return depths
```

## JavaScript Solution:

```javascript
function parseNestedParens(parenString) {
    var groups = parenString.split(/\s+/);
    var depths = [];

    for(var i = 0; i < groups.length; i++) {
        var group = groups[i];
        var maxDepth = 0;
        var currentDepth = 0;

        for(var j = 0; j < group.length; j++) {
            if(group[j] == '(') {
                currentDepth += 1;
                if(currentDepth > maxDepth) {
                    maxDepth = currentDepth;
                }
            } else if(group[j] == ')') {
                currentDepth -= 1;
            }
        }
