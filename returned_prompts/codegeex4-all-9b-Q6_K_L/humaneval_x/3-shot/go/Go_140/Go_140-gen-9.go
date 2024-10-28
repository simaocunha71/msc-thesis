    result := ""
    space_count := 0

    for _, c := range text {
        if c == ' ' {
            space_count += 1
            if space_count == 1 {
                result += "_"
            }else if space_count == 2 {
                result += "-"
            }
        }else {
            space_count = 0
            result += string(c)
        }
    }
    return result
}

