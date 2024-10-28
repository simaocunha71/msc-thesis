
// The problem can be solved using a greedy approach. 
// We will iterate over the strings and check if we have a closing bracket 
// without a corresponding opening bracket. If we do, we add it to a list of 
// unmatched closing brackets. If we encounter an opening bracket, we check 
// if there's a corresponding closing bracket in the list of unmatched brackets. 
// If there is, we remove it from the list, otherwise, we return 'No'. 
// If we finish iterating over the strings and the list of unmatched brackets 
// is empty, we return 'Yes', otherwise we return 'No'.

// Initialize a list of unmatched closing brackets.
unmatched := []rune{}

// Iterate over the strings.
for _, str := range lst {
    // Iterate over the characters in the string.
    for _, char := range str {
        if char == '(' {
            // If the character is an opening bracket, add it to the list.
            unmatched = append(unmatched, char)
        } else if char == ')' {
            // If the character is a closing bracket.
            if len(unmatched) > 0 {
                // If there's an opening bracket in the list, remove it.
                unmatched = unmatched[:len(unmatched)-1]
            } else {
                // If there's no opening bracket in the list, return 'No'.
                return "No"
            }
        }
    }
}

// If there's any unmatched opening bracket in the list, return 'No'.
if len(unmatched) > 0 {
    return "No"
}

// Return 'Yes' if we've made it this far.
return "Yes"
}
*/

func MatchParens(lst []string) string {
	unmatched := 0
	for _, str := range lst {
		for _, char := range str {
			switch char {
			case '(':
				unmatched++
			case ')':
				if unmatched == 0