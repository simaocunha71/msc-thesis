    result := ""
    space_count := 0
    for _, c := range text {
        if c == ' ' {
            space_count += 1
            if space_count == 1 {
                result += "_"
            } else if space_count == 2 {
                result += "-"
                space_count = 0
            }
        } else {
            result += string(c)
            space_count = 0
        }
    }
    return result
}