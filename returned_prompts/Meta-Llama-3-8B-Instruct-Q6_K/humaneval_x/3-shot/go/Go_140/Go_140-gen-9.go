    var result string
    var current_char rune
    var consecutive_spaces int

    for _, char := range text {
        if char == ' ' {
            if consecutive_spaces == 0 {
                result += "_"
                consecutive_spaces = 1
            } else {
                result += "-"
                consecutive_spaces = 1
            }
        } else {
            if consecutive_spaces > 0 {
                result += "_"
                consecutive_spaces = 0
            }
            result += string(char)
        }
        current_char = char
    }
    return result
}