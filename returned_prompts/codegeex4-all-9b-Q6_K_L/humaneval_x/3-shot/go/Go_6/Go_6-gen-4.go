    result := make([]int, 0)
    max_depth := 0
    current_depth := 0

    for _, c := range strings.Split(paren_string, " "){
        for _, c := range c {
            if c == '(' {
                current_depth += 1
                max_depth = math.Max(float64(max_depth), float64(current_depth))
            }else if c== ')'{
                current_depth -= 1
            }
        }
        result = append(result, max_depth)
        current_depth = 0
        max_depth = 0
    }
    return result
}



