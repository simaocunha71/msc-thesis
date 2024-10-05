    stack := make([]rune,0)
    for _, c := range brackets {
        if c == '(' {
            stack = append(stack, c)
        } else if c == ')' {
            if len(stack) == 0 {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}  // stack is empty if all brackets were correctly paired.  If there are any remaining open brackets, then there's a mismatch.