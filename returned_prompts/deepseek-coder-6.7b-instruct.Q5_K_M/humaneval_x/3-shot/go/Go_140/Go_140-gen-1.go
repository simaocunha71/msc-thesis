    result := ""
    count := 0
    for _, c := range text {
        if c == ' ' {
            count += 1
            if count == 2 {
                result += "-"
                count = 1
            }
        } else {
            if count > 0 {
                if count == 1 {
                    result += "_"
                }
                result += string(c)
                count = 0
            } else {
                result += string(c)
            }
        }
    }
    return result
}



