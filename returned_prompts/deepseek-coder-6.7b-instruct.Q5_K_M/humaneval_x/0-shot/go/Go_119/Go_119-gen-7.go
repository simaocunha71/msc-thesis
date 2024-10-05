
// We will use the stack data structure to solve this problem. 
// We will iterate through each string in the list and for each character 
// if it's an open parenthesis '(', we will push it into the stack. 
// If it's a close parenthesis ')', we will pop an element from the stack 
// and check if it's a matching pair. If not, we will return 'No'. 
// If the stack is empty at the end, we will return 'Yes', otherwise 'No'.

	// Initialize a stack
	stack := []rune{}

	// Iterate through each string in the list
	for _, str := range lst {
		// Iterate through each character in the string
		for _, ch := range str {
			// If it's an open parenthesis, push it into the stack
			if ch == '(' {
				stack = append(stack, ch)
			} else {
				// If it's a close parenthesis
				if len(stack) == 0 {
					// and the stack is empty, return 'No'
					return "No"
				}
				// Pop an element from the stack
				stack = stack[:len(stack)-1]
			}
		}
	}

	// If the stack is empty, return 'Yes'
	if len(stack) == 0 {
		return "Yes"
	}
	// Otherwise, return 'No'
	return "No"
}


func main() {
		fmt.Println(MatchParens([]string{"()(", ")"})) // Yes
		fmt.Println(MatchParens([]string{")", ")"})) // No
}























































































































