const separateParenGroups = (paren_string) => {
    const result = [];
    const stack = [];
    let current = '';
    for (let i = 0; i < paren_string.length; i++) {
        const char = paren_string[i];
        if (char === '(') {
            stack.push(char);
        } else if (char === ')') {
            const top = stack.pop();
            if (top === '(') {
                current += char;
            } else {
                stack.push(top);
                stack.push(char);
            }
        } else {
            current += char;
        }
    }
    while (stack.length) {
        current += stack.pop();
    }
    result.push(current);
    return result;
}