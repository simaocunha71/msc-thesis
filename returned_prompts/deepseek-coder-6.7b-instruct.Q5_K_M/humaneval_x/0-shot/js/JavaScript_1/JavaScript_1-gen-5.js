let stack = [];
let output = [];
let temp = '';

for (let i = 0; i < paren_string.length; i++) {
    if (paren_string[i] === '(') {
        stack.push(paren_string[i]);
        temp += paren_string[i];
    }
    if (paren_string[i] === ')') {
        stack.pop();
        temp += paren_string[i];
        if (stack.length === 0) {
            output.push(temp);
            temp = '';
        }
    }
}
return output;
}

console.log(separateParenGroups('(  )  (( ))  (( )( ))')); // ['()', '(())', '(()())']

*/

/*
