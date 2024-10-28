    result := make([]int, 0)
    stack := make([]int, 0)

    for _, c := range strings.Split(paren_string, " ") {
        for _, d := range []rune(c) {
            if d == '(' {
                stack = append(stack, len(stack) + 1)
            } else if d == ')' {
                stack = stack[:len(stack) - 1]
            }
        }
        result = append(result, len(stack))
    }
    return result
}