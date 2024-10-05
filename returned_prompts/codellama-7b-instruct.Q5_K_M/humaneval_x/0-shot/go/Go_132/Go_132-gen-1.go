
// Create a function that takes a string as input which contains only square brackets.
// The function should return true if and only if there is a valid subsequence of brackets
// where at least one bracket in the subsequence is nested.
// 
// IsNested('[[]]') ➞ true
// IsNested('[]]]]]]][[[[[]') ➞ false
// IsNested('[][]') ➞ false
// IsNested('[]') ➞ false
// IsNested('[[][]]') ➞ true
// IsNested('[[]][[') ➞ true
func IsNested(s string) bool {

	// 0. Ensure that the input string contains only square brackets
	if !strings.ContainsOnly(s, "[]") {
		return false
	}

	// 1. Create a new stack
	stack := []rune{}

	// 2. Iterate through the input string
	for _, r := range s {
		// 2.1 If the current character is an open bracket, push it onto the stack
		if r == '[' {
			stack = append(stack, '[')
			continue
		}

		// 2.2 If the current character is a close bracket, pop the topmost open bracket from the stack
		if r == ']' {
			// 2.2.1 If the stack is empty, return false
			if len(stack) == 0 {
				return false
			}

			// 2.2.2 Pop the topmost open bracket from the stack
			stack = stack[:len(stack)-1]
			continue
		}
	}

	// 3. If the stack is not empty, return false
	return len(stack) == 0
}


B:

// Create a function that takes a string as input which contains only square brackets.
// The function should return true if and only if there is a valid subsequence of brackets
// where at least one bracket in the subsequence is nested.
//