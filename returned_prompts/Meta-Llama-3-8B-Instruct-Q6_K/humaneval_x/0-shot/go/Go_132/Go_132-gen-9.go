```go
func IsNested(s string) bool {
    stack := []rune{}
    for _, c := range s {
        if c == '[' {
            stack = append(stack, c)
        } else if c == ']' {
            if len(stack) == 0 {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) > 0
}
```

In this solution, we use a stack to keep track of the opening brackets. We iterate over the input string, and for each character, we check if it's an opening bracket ( '[' ) or a closing bracket ( ']' ). If it's an opening bracket, we push it onto the stack. If it's a closing bracket, we check if the stack is empty. If it is, it means there's no matching opening bracket, so we return false. Otherwise, we pop the opening bracket from the stack. After iterating over the entire string, we check if the stack is not empty. If it's not, it means there are unmatched opening brackets, so we return true. If the stack is empty, it means all brackets were properly matched, so we return false. 

This solution has a time complexity of O(n), where n is the length of the input string, and a space complexity of O(n) as well, since in the worst case, we might need to store all characters in the stack. 