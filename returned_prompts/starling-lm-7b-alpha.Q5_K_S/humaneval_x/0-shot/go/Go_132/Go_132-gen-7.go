
func IsNested(s string) bool {
    stack := []rune{}
    for _, r := range s {
        if r == '[' {
            stack = append(stack, r)
        } else if r == ']' {
            if len(stack) > 0 && stack[len(stack)-1] == '[' {
                stack = stack[:len(stack)-1]
            } else {
                stack = []rune{}
            }
        }
    }
    return len(stack) > 0
}






func IsNested(s string) bool {
    stack := []rune{}
    for _, r := range s {
        if r == '[' {
            stack = append(stack, r)
        } else if r == ']' {
            if len(stack) > 0 && stack[len(stack)-1] == '[' {
                stack = stack[:len(stack)-1]
            } else {
                stack = []rune{}
            }
        }
    }
    return len(stack) > 0
}










func IsNested(s string) bool {
    stack := []rune{}
    for _, r := range s {
        if r == '[' {
            stack = append(stack, r)
        } else if r == ']' {
            if len(stack) > 0 && stack[len(stack)-1] == '[' {
                stack = stack[:len(stack)-1]
            } else {
                stack = []rune{}
            }
        }
    }
    return len(stack) > 0
}















































































































