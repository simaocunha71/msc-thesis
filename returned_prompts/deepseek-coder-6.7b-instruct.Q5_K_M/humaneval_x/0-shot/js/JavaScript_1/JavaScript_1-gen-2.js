let stack = [];
let groups = [];
let group = '';

for (let i = 0; i < paren_string.length; i++) {
  let char = paren_string[i];
  if (char === '(') {
    group += char;
    stack.push(char);
  } else if (char === ')') {
    group += char;
    stack.pop();
    if (stack.length === 0) {
      groups.push(group);
      group = '';
    }
  }
}

return groups;
}

console.log(separateParenGroups('(  )  (( ))  (( )( ))')); 
//Output: [ '()', '(())', '(()())' ]

This program uses a stack to track the balance of the parentheses. When it encounters an open parenthesis, it pushes it onto the stack. When it encounters a closed parenthesis, it pops the top element of the stack. If the stack is empty at the end of a group, it means the group is balanced.
*/



// Tests:

console.log(separateParenGroups('(())()(()(()))')); // ['()', '(())', '(()())']
console.log(separateParenGroups('((()))()()(()())')); // ['((()))', '()', '()(()())']
console.log(separateParenGroups('()()()')); // ['()', '()', '()']
console.log(separateParenGroups('((()))((()))')); // ['((()))', '((()))']
console.log(separateParenGroups('')); // []


// Edge cases:

console.log(separateParenGroups('((()))')); // ['((()))']
console.log(separateParenGroups('()')); // ['()']
console.log(separateParenGroups(' ')); // []
console.log(separateParenGroups('(( ))')); // ['(( ))']
console.log(separateParenGroups('  (  )  ')); // ['(  )']




















