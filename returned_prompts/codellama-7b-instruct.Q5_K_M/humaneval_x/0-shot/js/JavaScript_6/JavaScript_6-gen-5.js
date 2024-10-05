const parseNestedParens = (paren_string) => {
    let stack = [];
    let max = 0;
    let last_level = 0;
    for (let i = 0; i < paren_string.length; i++) {
        if (paren_string[i] === '(') {
            stack.push(paren_string[i]);
            last_level = max;
            max++;
        } else if (paren_string[i] === ')') {
            stack.pop();
            if (stack.length === 0) {
                max = last_level;
            }
        }
    }
    return max;
}

