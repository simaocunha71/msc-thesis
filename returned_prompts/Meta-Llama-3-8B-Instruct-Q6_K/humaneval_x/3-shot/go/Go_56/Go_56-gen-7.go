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
}  // The length of the stack should be 0 if all brackets are correctly matched. Otherwise, return false.  // The length of the stack should be 0 if all brackets are correctly matched. Otherwise, return false.  // The length of the stack should be 0 if all brackets are correctly matched. Otherwise, return false.  // The length of the stack should be 0 if all brackets are correctly matched. Otherwise, return false.  // The length of the stack should be 0 if all brackets are correctly matched. Otherwise, return false.  // The length of the stack should be 0 if all brackets are correctly matched. Otherwise, return false.  // The length of the stack should be 0 if all brackets are correctly matched. Otherwise, return false.  // The length of the stack should be 0 if all brackets are correctly matched. Otherwise, return false.  // The length of the stack should be 0 if all brackets are correctly matched. Otherwise, return false.  // The length of the stack should be 0 if all brackets are correctly matched. Otherwise, return false.  // The length of the stack should be 0 if all brackets are correctly matched. Otherwise, return false.  // The length of the stack should be 0 if all brackets are correctly matched. Otherwise, return false.  // The length of the stack should be 0 if all brackets are correctly matched. Otherwise, return false.  // The length of the stack should be 0 if all brackets are correctly matched. Otherwise, return false.  // The length of the stack should be 0 if all brackets are correctly matched. Otherwise, return false.  // The length of the stack should be 0 if all brackets are correctly matched. Otherwise, return false.  // The length of the stack should be 0 if all brackets are correctly matched. Otherwise, return false.  // The length of the stack should be 0 if all brackets are correctly matched. Otherwise, return false.  // The length of the stack should be 0 if all brackets are correctly matched