
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
    if len(s) == 0 {
        return false
    }
    stack := make([]int, 0)
    for _, char := range s {
        if char == '[' {
            stack = append(stack, 1)
        } else if char == ']' {
            stack = stack[:len(stack)-1]
            if len(stack) == 0 {
                return false
            }
            if stack[len(stack)-1] == 1 {
                stack[len(stack)-1] = 0
                continue
            }
            stack[len(stack)-1] = stack[len(stack)-1] + 1
        }
    }
    return len(stack) == 0
}
