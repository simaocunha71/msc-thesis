    result := make([]int, 0)
    splitted := strings.Split(paren_string, " ")

    for _, group := range splitted {
        count := 0
        max_count := 0
        for _, char := range group {
            if string(char) == "(" {
                count += 1
                if count > max_count {
                    max_count = count
                }
            } else if string(char) == ")" {
                count -= 1
            }
        }
        result = append(result, max_count)
    }

    return result
}



