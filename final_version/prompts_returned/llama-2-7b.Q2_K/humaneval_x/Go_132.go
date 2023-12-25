
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
	var i int
	for ;i<len(s);i=i+3;{
		if s[:i] == "[]" && isValidSubsequence(&s, i, len(s)-1-i) {
			return true
		} else if s[i:i+2] == "[[[" && isValidSubsequenceAfterOpeningBracket(&s, i, len(s)-1-i)) {
			if (len(s)-1-i)+3 >= len(s) ||  isValidSubsequenceAfterClosingBracket(&s, (len(s)-1-i)+3, s[len(s)-1-i:]) {
				return true
			}
		} else if isValidSubsequenceAfterOpeningBracket(&s, i, len(s)-1-i)) {
			if (len(s)-1-i)+3 >= len(s) ||  isValidSubsequence(&s, i+2, len(s)-1-i+2) {
				return true
			}
		} else if s[:i] == "]]" && isValidSubsequenceAfterClosingBracket(&s, i, len(s)-1-i)) {
			if (len(s)-1-i)+3 >= len(s) ||  isValidSubsequenceAfterOpeningBracket(&s, (len(s)-1-i)+3, s[(len(s)-1-i)-4