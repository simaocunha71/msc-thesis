
// You are given a list of two strings, both strings consist of open
// parentheses '(' or close parentheses ')' only.
// Your job is to check if it is possible to concatenate the two strings in
// some order, that the resulting string will be good.
// A string S is considered to be good if and only if all parentheses in S
// are balanced. For example: the string '(())()' is good, while the string
// '())' is not.
// Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.
// 
// Examples:
// MatchParens(['()(', ')']) == 'Yes'
// MatchParens([')', ')']) == 'No'
func MatchParens(lst []string) string {
	if len(lst) < 2 {
		return "no"
	} else if strings.HasPrefix(lst[0], lst[len(lst)-1]) {
		return "no"
	}

	for i, v := range lst {
		if v == ')' && i != len(lst)-1 {
			return "no"
		} else if i != 0 && strings.Contains(v, "((") || v == ")(") {
			return "yes"
		}
	}

	// A string is good when the first and last element are matching brackets
	if lst[len(lst)-1] == ')' && lst[0] == '(' {
		return "yes"
	}

	return ""
}
