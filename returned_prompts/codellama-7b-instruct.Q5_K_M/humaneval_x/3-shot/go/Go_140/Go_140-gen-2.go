    var result string
    var current_string string
    var is_space bool
    var consecutive_spaces int

    for _, c := range text {
        if c == ' ' {
            is_space = true
            consecutive_spaces += 1
        } else {
            is_space = false
            consecutive_spaces = 0
        }

        if is_space {
            current_string += "_"
            if consecutive_spaces > 1 {
                current_string += "-"
            }
        } else {
            current_string += string(c)
        }
    }
    return current_string
}



