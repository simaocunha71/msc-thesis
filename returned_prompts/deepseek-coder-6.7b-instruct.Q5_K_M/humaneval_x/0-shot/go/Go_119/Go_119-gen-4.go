
// First, I'll define a helper function to check if a string is balanced.
// This function will iterate over the characters in the string, keeping a count of open parentheses.
// If it encounters a closed parenthesis without a corresponding open parenthesis, it returns false.
// If it finishes without encountering any unmatched closed parentheses, it returns true.

func isBalanced(s string) bool {
	count := 0
	for _, c := range s {
		if c == '(' {
			count++
		} else if c == ')' {
			if count == 0 {
				return false
			}
			count--
		}
	}
	return count == 0
}

// Then I'll iterate over the strings in the input list, checking if they are balanced.
// If any string is balanced, I'll return 'Yes'. If none are balanced, I'll return 'No'.

for _, s := range lst {
	if isBalanced(s) {
		return "Yes"
	}
}
return "No"
}

// Test cases:
// fmt.Println(MatchParens([]string{"()(", ")"})) // Should print "Yes"
// fmt.Println(MatchParens([]string{")", ")"})) // Should print "No"
// fmt.Println(MatchParens([]string{"((", ")"})) // Should print "Yes"
// fmt.Println(MatchParens([]string{"(", ")"})) // Should print "No"
// fmt.Println(MatchParens([]string{"()", "()"})) // Should print "Yes"
// fmt.Println(MatchParens([]string{"()", "(("})) // Should print "No"
// fmt.Println(MatchParens([]string{"(", "("})) // Should print "Yes"
// fmt.Println(MatchParens([]string{"(((", ")))("})) // Should print "No"
// fmt.Println(MatchParens([]string{"(((", ")))("})) // Should print "No"
func main() {
	fmt.Println(MatchP