
// Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
// separate those group into separate strings and return the list of those.
// Separate groups are balanced (each open brace is properly closed) and not nested within each other
// Ignore any spaces in the input string.
// >>> SeparateParenGroups('( ) (( )) (( )( ))')
// ['()', '(())', '(()())']
func SeparateParenGroups(paren_string string) []string {
	var paren_groups []string
	var current_group string
	var stack []rune

	for _, c := range paren_string {
		switch c {
		case '(':
			stack = append(stack, c)
		case ')':
			// If we have a closing paren that doesn't match the last opening paren, ignore
			if len(stack) == 0 || stack[len(stack)-1] != '(' {
				continue
			}

			stack = stack[:len(stack)-1]

			// If we have an empty stack, it means that we have a balanced group
			if len(stack) == 0 {
				paren_groups = append(paren_groups, current_group)
				current_group = ""
			}
		default:
			current_group += string(c)
		}
	}

	return paren_groups
}
