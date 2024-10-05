    var open_bracket_count int = 0

    for _, c := range s {
        if c == '[' {
            open_bracket_count += 1
        } else if c == ']' {
            open_bracket_count -= 1
        }
        if open_bracket_count < 0 {
            return false
        }
    }
    return open_bracket_count == 0
}



