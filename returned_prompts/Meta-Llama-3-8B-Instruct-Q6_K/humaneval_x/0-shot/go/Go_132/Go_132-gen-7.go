```go
func IsNested(s string) bool {
    stack := []byte{}
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



This function uses a stack to keep track of the opening brackets. It iterates over the input string, and for each character, it checks if it's an opening bracket ( '[' ) or a closing bracket ( ']' ). If it's an opening bracket, it pushes it onto the stack. If it's a closing bracket, it checks if the stack is empty (which means there's no corresponding opening bracket) or not. If the stack is empty, it returns false. If the stack is not empty, it pops the opening bracket from the stack. After iterating over the entire string, it checks if the stack is empty. If it's not empty, it means there's at least one opening bracket that was not closed, so it returns true. If the stack is empty, it means all brackets were properly closed, so it returns false.