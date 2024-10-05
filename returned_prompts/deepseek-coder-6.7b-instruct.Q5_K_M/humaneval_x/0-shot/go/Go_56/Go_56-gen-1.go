
// We will use a stack to keep track of the opening brackets. When we encounter a closing bracket, we will check if the stack is empty or the top of the stack contains the corresponding opening bracket. If it's not, we return false. If it is, we pop the top of the stack.

// B:

// First, we initialize an empty stack.

	stack := make([]rune, 0)

// Then, for each character in the string, we check if it's an opening bracket or a closing bracket.

	for _, c := range brackets {

		switch c {

		case '<':

			// If it's an opening bracket, we push it onto the stack.

			stack = append(stack, c)

		case '>':

			// If it's a closing bracket, we check if the stack is empty or the top of the stack contains the corresponding opening bracket.

			if len(stack) == 0 || stack[len(stack)-1] != '<' {

				return false

			}

			// If it's the case, we pop the top of the stack.

			stack = stack[:len(stack)-1]

		default:

			// If it's neither an opening nor a closing bracket, we return false.

			return false

		}

	}

// Finally, we check if the stack is empty. If it's not, we return false. If it is, we return true.

	return len(stack) == 0

}

```

## Code Explanation

The function `CorrectBracketing` takes a string of brackets as input and returns a boolean indicating whether the brackets are correctly nested.

The function works by using a stack to store the opening brackets and checking for matching closing brackets.

If an opening bracket is encountered, it is pushed onto the stack. If a closing bracket is encountered, it is checked to see if the top of the stack contains the corresponding opening bracket. If it does, the opening bracket is popped from the stack; if it does not, the function returns `false`.