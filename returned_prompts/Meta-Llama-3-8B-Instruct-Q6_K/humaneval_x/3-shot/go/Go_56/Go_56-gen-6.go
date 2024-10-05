    stack := make([]byte, 0)

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
}  // Time complexity is O(n) where n is the length of the brackets string. Space complexity is also O(n).  // This solution works by maintaining a stack of opening brackets. When we encounter a closing bracket, we check if the stack is empty. If it is, that means there's no matching opening bracket and we return false. If the stack is not empty, we pop the opening bracket from the stack. At the end, if the stack is empty, that means all brackets are correctly paired and we return true. If the stack is not empty, that means there are unmatched opening brackets and we return false.