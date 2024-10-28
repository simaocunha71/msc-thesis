```
func CorrectBracketing(brackets string) bool {
    stack := []rune{}
    for _, bracket := range brackets {
        if bracket == '<' {
            stack = append(stack, '<')
        } else if bracket == '>' {
            if len(stack) == 0 || stack[len(stack)-1] != '<' {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}
```
In this solution, we use a stack to keep track of the opening brackets. When we encounter a closing bracket, we check if the stack is empty or if the top of the stack is not an opening bracket. If either condition is true, we return false. If the stack is empty at the end, we return true. If the stack is not empty, it means there are unmatched opening brackets, so we return false. This solution has a time complexity of O(n), where n is the length of the input string, and a space complexity of O(n) for the stack.