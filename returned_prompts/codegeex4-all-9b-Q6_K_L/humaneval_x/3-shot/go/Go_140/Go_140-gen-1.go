    var result string
    var current_char rune
    var current_char_is_space bool

    for _, c := range text {
        if c == ' '{
            if current_char_is_space{
                continue
            }

            current_char_is_space = true
            current_char = c
        }else{
            current_char_is_space = false
            current_char = c
        }

        result += string(current_char)
    }

    return result
}

