    var result []int
    var current_depth int

    for _, s := range strings.Split(paren_string," ") {
        current_depth = 0
        for _, c := range s {
            if c=='(' {
                current_depth += 1
            } else if c == ')' {
                current_depth -= 1
            }
        }
        result = append(result, current_depth)
    }
    return result
}



