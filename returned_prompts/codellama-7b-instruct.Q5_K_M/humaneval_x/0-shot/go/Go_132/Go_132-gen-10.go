
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
    var count int
    for _, v := range s {
        if v == '[' {
            count++
        } else if v == ']' {
            count--
        }
        if count < 0 {
            return false
        }
    }
    return count == 0
}
