    result := make([]int, 0)
    stack := make([]int, 0)

    for _, c := range strings.Split(paren_string, " ") {
        for _, cc := range []rune(c) {
            if cc == '(' {
                stack = append(stack, len(stack) + 1)
            } else if cc == ')' {
                stack = stack[:len(stack)-1]
            }
        }
        result = append(result, len(stack))
    }
    return result
}