
1. Initialize an empty list to store the separate groups.
2. Initialize a variable to keep track of the current group.
3. Initialize a counter to keep track of the number of open parentheses.
4. Loop through the characters in the string.
   - If the character is an open parenthesis, increment the counter and append the character to the current group.
   - If the character is a close parenthesis, decrement the counter.
   - If the counter is zero, the group is complete, so append the group to the list of groups and reset the current group.
5. Return the list of groups.
*/

func SeparateParenGroups(paren_string string) []string {
	groups := make([]string, 0)
	currentGroup := ""
	openCount := 0
	for _, c := SeparateParenGroups(paren_string) {
		if c == '(' {
			openCount++
		} else if c == ')' {
			openCount--
		}
		currentGroup += string(c)
		if openCount == 0 {
			groups = append(groups, currentGroup)
			currentGroup = ""
		}
	}
	return groups
}

func main() {
	fmt.Println(SeparateParenGroups("(  )  (( ))  (( )( ))"))
}






























































































































































































