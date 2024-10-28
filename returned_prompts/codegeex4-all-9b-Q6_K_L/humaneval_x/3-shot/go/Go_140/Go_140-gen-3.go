    result := ""
    space_count := 0

    for _, c := range text {
        if c == ' ' {
            space_count += 1
            if space_count > 2 {
                result += "-"
            } else {
                result += "_"
            }
        } else {
            space_count = 0
            result += string(c)
        }
    }

    return result
}

