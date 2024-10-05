    result := make([]int, 0)
    groups := strings.Fields(paren_string)

    for _, group := range groups {
        count, max := 0, 0
        for _, char := range group {
            if char == '(' {
                count++
                if count > max {
                    max = count
                }
            } else if char == ')' {
                count--
            }
        }
        result = append(result, max)
    }

    return result
}



