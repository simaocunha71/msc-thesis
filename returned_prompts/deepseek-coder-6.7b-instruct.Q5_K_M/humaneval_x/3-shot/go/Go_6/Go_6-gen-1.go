    result := make([]int, 0)
    groups := strings.Fields(paren_string)

    for _, group := range groups {
        count, max := 0, 0
        for _, c := range group {
            switch c {
            case '(':
                count++
                if count > max {
                    max = count
                }
            case ')':
                count--
            }
        }
        result = append(result, max)
    }
    return result
}



