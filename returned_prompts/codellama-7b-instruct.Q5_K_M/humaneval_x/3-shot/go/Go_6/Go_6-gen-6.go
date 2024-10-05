    var max_depth = 0
    var current_depth = 0
    var result = make([]int, 0)
    for _, c := range paren_string {
        if c == '(' {
            current_depth += 1
        }else if c== ')'{
            current_depth -= 1
        }
        if current_depth > max_depth {
            max_depth = current_depth
        }
        if c == ' ' {
            result = append(result, max_depth)
            max_depth = 0
        }
    }
    result = append(result, max_depth)
    return result
}



