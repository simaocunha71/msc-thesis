
// Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
// separate those group into separate strings and return the list of those.
// Separate groups are balanced (each open brace is properly closed) and not nested within each other
// Ignore any spaces in the input string.
// >>> SeparateParenGroups('( ) (( )) (( )( ))')
// ['()', '(())', '(()())']
func SeparateParenGroups(paren_string string) []string {
	open_paren_count := 0
	close_paren_count := 0
	group_start := 0
	groups := []string{}
	for i := 0; i < len(paren_string); i++ {
		c := paren_string[i]
		if c == '(' {
			open_paren_count++
			group_start = i
		}
		if c == ')' {
			close_paren_count++
			if open_paren_count == close_paren_count {
				groups = append(groups, paren_string[group_start+1:i])
				open_paren_count = 0
				close_paren_count = 0
			}
		}
	}
	return groups
}

// Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
// separate those group into separate strings and return the list of those.
// Separate groups are balanced (each open brace is properly closed) and not nested within each other
// Ignore any spaces in the input string.
// >>> SeparateParenGroups('( ) (( )) (( )( ))')
// ['()', '(())', '(()())']
func SeparateParenGroups(paren_string string) []string {
	open_paren_count := 0
	close_paren_count := 0
	group_start := 0
	groups := []string{}
	for i := 0; i < len(paren_string); i++