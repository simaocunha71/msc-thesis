    result := make([]int, 0)
    split_string := strings.Split(paren_string, " ")

    for _, group := range split_string {
        count := 0
        max := 0
        for _, char := range group {
            if string(char) == "(" {
                count += 1
                if count > max {
                    max = count
                }
            } else if string(char) == ")" {
                count -= 1
            }
        }
        result = append(result, max)
    }
    return result
}



