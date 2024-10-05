    result := ""
    count := 0
    for _, c := range text {
        if c == ' ' {
            count++
            if count == 2 {
                result += "-"
                count = 1
            }
        } else {
            if count > 0 {
                result += "_"
                count = 0
            }
            result += string(c)
        }
    }
    if count > 0 {
        result += "_"
    }
    return result
}



