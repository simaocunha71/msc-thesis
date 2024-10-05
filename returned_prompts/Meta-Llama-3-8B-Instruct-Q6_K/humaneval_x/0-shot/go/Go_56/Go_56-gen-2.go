```
func CorrectBracketing(brackets string) bool {
    stack := []rune{}
    for _, r := range brackets {
        if r == '<' {
            stack = append(stack, r)
        } else if r == '>' {
            if len(stack) == 0 {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}
```
Explanation:

*   We use a stack to keep track of the opening brackets.
*   For each character in the input string, we check if it's an opening bracket (`<`) or a closing bracket (`>`).
*   If it's an opening bracket, we push it onto the stack.
*   If it's a closing bracket, we check if the stack is empty. If it is, we return `false` because there's no corresponding opening bracket.
*   If the stack is not empty, we pop the opening bracket from the stack.
*   Finally, we return `true` if the stack is empty (meaning all opening brackets had corresponding closing brackets) and `false` otherwise.