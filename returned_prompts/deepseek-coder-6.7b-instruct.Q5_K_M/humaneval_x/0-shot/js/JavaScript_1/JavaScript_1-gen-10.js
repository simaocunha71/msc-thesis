let stack = [];
let group = [];
	let groups = [];

	for (let i = 0; i < paren_string.length; i++) {
		if (paren_string[i] === '(') {
			stack.push(paren_string[i]);
			group.push(paren_string[i]);
		} else if (paren_string[i] === ')') {
			stack.pop();
			group.push(paren_string[i]);
			if (stack.length === 0) {
				groups.push(group.join(''));
				group = [];
			}
		}
	}

	return groups;
}

console.log(separateParenGroups('(  )  (( ))  (( )( ))'));

This program will return all separate groups of parentheses as separate strings in an array. It uses a stack to keep track of open and closed parentheses. When a closing parenthesis is found, it pops the top of the stack. When the stack is empty, it means a group of parentheses has ended, so it adds this group to the list of groups.
```

---

### Solution 2:

```javascript
