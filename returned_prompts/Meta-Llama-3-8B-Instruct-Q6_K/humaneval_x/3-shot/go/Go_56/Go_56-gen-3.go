    stack := make([]rune, 0)
    for _, c := range brackets {
        if c == '<' {
            stack = append(stack, c)
        } else if c == '>' {
            if len(stack) == 0 {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}  // This function is used to check if every opening bracket has a corresponding closing bracket. It uses a stack to keep track of the opening brackets. It iterates over the string, pushing opening brackets onto the stack and popping them when it encounters a closing bracket. If it encounters a closing bracket when the stack is empty, it immediately returns false. If it has any opening brackets left in the stack at the end of the string, it also returns false. Otherwise, it returns true.