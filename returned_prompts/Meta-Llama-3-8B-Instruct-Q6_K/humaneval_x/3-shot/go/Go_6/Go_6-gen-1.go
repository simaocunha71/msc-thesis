    result := make([]int, 0)
    current_depth := 0

    for _, c := range strings.Split(paren_string, " ") {
        depth := 0
        for _, d := range []rune(c) {
            if d == '(' {
                depth += 1
            }else if d == ')'){
                depth -= 1
            }
        }
        result = append(result, depth)
    }
    return result
}