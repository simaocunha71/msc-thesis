
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
		return "Yes"
	}

	var sum int = 0
	for _, a := range lst {
		sum += len(a[1:])
	}

	openCount, closeCount := 0, sum

	for i := 0; i < len(lst); i++ {
		if openCount == len(lst) && i == (len(lst)-1) && lst[i][1:] != "" {
			return "No"
		}
		open, close := -1, -1
		for _, c := range lst[i] {
			switch c {
			case ')':
				close++
			case '(':
				open++
			}
		}
		if openCount == 0 && close != 0 || (openCount > 0 && close == 0) {
			return "Yes"
		} else if openCount < 0 && closeCount >= 0 {
			return "No"
		}
		if openCount == len(lst)-1 || i+1 >= len(lst) {
			openCount++
		} else {
			sum--
		}
		closeCount -= 1
		if close < 0 && openCount != -