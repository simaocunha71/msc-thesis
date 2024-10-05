
// Create a function that takes a string as input which contains only square brackets.
// The function should return true if and only if there is a valid subsequence of brackets
// where at least one bracket in the subsequence is nested.
// 
// IsNested('[[]]') ➞ true
// IsNested('[]]]]]]][[[[[]') ➞ false
// IsNested('[][]') ➞ false
// IsNested('[]') ➞ false
// IsNested('[[][]]') ➞ true
// IsNested('[[]][[') ➞ true
func IsNested(s string) bool {
	n := len(s)
	if n == 0 {
		return false
	}
	if n == 2 {
		return s == "[]"
	}
	l, r := 0, 0
	for i := 0; i < n; i++ {
		if s[i] == '[' {
			l++
		} else if s[i] == ']' {
			r++
		}
		if l > r {
			return false
		}
	}
	return l == r
}
