    var result string = ""
    var consecutive_spaces_count int = 0

    for _, c := range text {
        if c == ' ' {
            consecutive_spaces_count += 1
            if consecutive_spaces_count >= 3 {
                result += "-"
                consecutive_spaces_count = 0
            }
        }else {
            result += string(c)
            consecutive_spaces_count = 0
        }
    }
    return result
}



