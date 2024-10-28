const isNested = (string) => {
    const stack = [];
    for (let bracket of string) {
        if (bracket === '[' || bracket === ']') {
            if (bracket === '[') stack.push(bracket);
            else {
                if (stack.pop() !== '[') return false;
            }
        }
    }
    return stack.length === 0;
}
