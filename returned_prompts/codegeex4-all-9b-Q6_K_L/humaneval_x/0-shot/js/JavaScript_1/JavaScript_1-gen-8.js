Here's a JavaScript solution using a stack to track the groups of parentheses:

```javascript
const separateParenGroups = (paren_string) => {
  let groups = [];
  let stack = [];
  let currentGroup = [];

  for (let i = 0; i < paren_string.length; i++) {
    let char = paren_string[i];

    if (char === '(') {
      stack.push(currentGroup);
      currentGroup = [];
    } else if (char === ')') {
      if (stack.length > 0) {
        currentGroup = stack.pop();
      }
      currentGroup.push(...currentGroup.reverse());
      currentGroup.push(`(${currentGroup.join('')})`);
      currentGroup = currentGroup.reverse();
    } else {
      currentGroup.push(char);
    }
  }

  return groups;
};

console.log(separateParenGroups('( ) (( )) (( )( ))')); // ['()', '(())', '(()())']
```

This solution works by iterating through each character in the input string. If the character is an open parenthesis, it pushes the current group onto the stack and starts a new group. If the character is a closed parenthesis, it pops the last group off the stack and adds it to the current group. If the character is not a parenthesis, it simply adds it to the current group. After iterating through all the characters, it returns the list of groups.