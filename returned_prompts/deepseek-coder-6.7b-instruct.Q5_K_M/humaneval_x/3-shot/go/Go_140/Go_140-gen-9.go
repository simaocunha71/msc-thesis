    result := ""
    count := 0

    for _, c := range text {
        if c == ' ' {
            count++
            if count == 2 {
                result += "-"
            }
        } else {
            if count >= 2 {
                result += "_"
            }
            result += string(c)
            count = 0
        }
    }

    return result
}



