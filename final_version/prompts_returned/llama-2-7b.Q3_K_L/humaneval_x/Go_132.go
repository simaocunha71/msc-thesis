
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
	if s == "" || len(s) < 2 {
		return false;
	}
	brackets := make(map[int]bool)
	for i := range s {
		if s[i] == '[' && brackets[len(s)-1-i] {
			return true
		} else if s[i] == ']' {
			brackets[len(s)-1-i] = false
		}
	}
	return false
}
