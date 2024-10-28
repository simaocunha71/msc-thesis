
// Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
// separate those group into separate strings and return the list of those.
// Separate groups are balanced (each open brace is properly closed) and not nested within each other
// Ignore any spaces in the input string.
// >>> SeparateParenGroups('( ) (( )) (( )( ))')
// ['()', '(())', '(()())']
func SeparateParenGroups(paren_string string) []string {
	paren_groups := []string{}
	current_group := ""
	for _, char := range paren_string {
		if char == '(' {
			current_group += char
		} else if char == ')' {
			current_group += char
			paren_groups = append(paren_groups, current_group)
			current_group = ""
		}
	}
	return paren_groups
}

