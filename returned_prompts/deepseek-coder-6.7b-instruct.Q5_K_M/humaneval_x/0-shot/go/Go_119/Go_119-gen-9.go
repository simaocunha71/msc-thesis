
// We will use a greedy approach to solve this problem.
// Start by checking if the first string has a balance of parentheses.
// If it does, then we can directly append the second string to the first string.
// If not, we have two options: we can either reverse the second string or
// reverse the order of the two strings and then reverse the second string.
// We will check both options and return 'Yes' if either of them results in a
// balanced parentheses string.
// If neither of the options results in a balanced string, we will return 'No'.
	
	check := func(s string) bool {
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
	
	for _, s := range lst {
		if check(s) {
			return "Yes"
		}
	}
	
	rev := func(s string) string {
		r := []rune(s)
		for i, j := 0, len(r)-1; i < j; i, j = i+1, j-1 {
			r[i], r[j] = r[j], r[i]
		}
		return string(r)
	}
	
	lst = []string{rev(lst[0]), rev(lst[1])}
	for _, s := range lst {
		if check(s) {
			return "Yes"
		}
	}
	
	return "No"
}
*/

func TestMatchParens(t *testing.T) {
	testCases := []struct {
		name string
		lst  []string
		want string
	}{
		{
			name: "test 1",
			lst:  []string{"()(", ")"},
			want: "Yes",
		},
		{
			name: "test 2",
			lst:  []