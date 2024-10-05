    for i, c := range paren_string {
        if c != '(' && c != ')' {
            continue A
        }
        // If we reach here, we know that c is '(' or ')'.
        // Count the number of parentheses until the next ')'.
        // If we don't find ')', then return an error.
        level := 0
        for j := i; j < len(paren_string); j++ {
            if paren_string[j] == ')' {
                break
            } else if paren_string[j] == '(' {
                level++
            }
        }
        if paren_string[i] == '(' {
            level = -level
        }
        return []int{level}
    }
    return nil
}
