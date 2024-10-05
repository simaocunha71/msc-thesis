    result := make([]int, 0)
    parts := strings.Split(paren_string, " ")

    for _, part := range parts {
        count := 0
        max := 0
        for _, char := range part {
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



