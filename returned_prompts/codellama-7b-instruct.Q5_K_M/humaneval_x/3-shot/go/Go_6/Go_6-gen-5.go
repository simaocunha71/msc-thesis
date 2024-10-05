    result := make([]int, 0)
    current_level := 0

    for _, c := range paren_string {
        if c == '(' {
            current_level += 1
        }else if c== ')' {
            current_level -= 1
        }

        if current_level > 0 {
            current_level = math.Max(current_level, result[len(result)-1])
        }

        if c == ' ' {
            result = append(result, current_level)
            current_level = 0
        }
    }
    return result
}



