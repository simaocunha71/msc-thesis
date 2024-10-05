
// Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
// separate those group into separate strings and return the list of those.
// Separate groups are balanced (each open brace is properly closed) and not nested within each other
// Ignore any spaces in the input string.
// >>> SeparateParenGroups('( ) (( )) (( )( ))')
// ['()', '(())', '(()())']
func SeparateParenGroups(paren_string string) []string {

	// Create a list to store the results
	paren_groups := make([]string, 0)

	// Create a stack to keep track of the paren groups
	stack := []string{}

	// Iterate through the string and parse the groups
	for i, char := range paren_string {
		if char == '(' {
			// If the character is a '(', push it onto the stack
			stack = append(stack, char)
		} else if char == ')' {
			// If the character is a ')', pop the top item from the stack and append it to the results
			// This will always be the last open brace for this group
			paren_groups = append(paren_groups, string(stack[len(stack)-1]))
			stack = stack[:len(stack)-1]
		}
	}

	// Check if there are any remaining items in the stack
	// If there are, then there are unmatched parens in the input
	if len(stack) > 0 {
		panic("There are unmatched parentheses in the input")
	}

	// Return the list of paren groups
	return paren_groups
}

// Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
// separate those group into separate strings and return the list of those.
// Separate groups are balanced (each open brace is properly closed) and not nested within each other
// Ignore any spaces in the input string.
// >>> SeparateParenGroups('( ) (( )) (( )( ))')
// ['()