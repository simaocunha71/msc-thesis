    result := make([]int, 0)
    split_strings := strings.Split(paren_string, " ")

    for _, str := range split_strings {
        current_max := 0
        current := 0
        for _, ch := range str {
            if ch == '(' {
                current += 1
                current_max = int(math.Max(float64(current_max), float64(current)))
            } else if ch == ')' {
                current -= 1
            }
        }
        result = append(result, current_max)
    }

    return result
}


