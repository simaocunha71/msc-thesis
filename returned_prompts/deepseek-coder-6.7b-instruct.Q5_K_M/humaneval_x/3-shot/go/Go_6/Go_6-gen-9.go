    result := make([]int, 0)
    groups := strings.Split(paren_string, " ")

    for _, group := range groups {
        count := 0
        maxCount := 0
        for _, char := range group {
            switch char {
            case '(':
                count++
                if count > maxCount {
                    maxCount = count
                }
            case ')':
                count--
            }
        }
        result = append(result, maxCount)
    }

    return result
}



