const isNested = (str) => {
	const stack = [];
	for (const char of str) {
		if (char === "[" && !stack.length) stack.push(char);
		else if (char === "]" && stack[stack.length - 1] === "[") stack.pop();
		else if (char === "]") stack.push(char);
	}
	return !stack.length;
}

