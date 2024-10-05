    var is_valid bool = true
    var digit_count int = 0
    var dot_count int = 0
    var extension string = ""
    var first_char rune = '0'
    var last_char rune = '0'

    for _, c := range strings.ToLower(file_name) {
        if c >= 'a' && c <= 'z' {
            last_char = c
        } else if c >= '0' && c <= '9' {
            digit_count += 1
            last_char = c
        } else if c == '.' {
            dot_count += 1
        }
    }

    if last_char >= '0' && last_char <= '9' {
        is_valid = false
    }

    if dot_count == 1 {
        parts := strings.Split(file_name, ".")
        extension = parts[len(parts)-1]
        if extension != "txt" && extension != "exe" && extension != "dll" {
            is_valid = false
        }
    } else {
        is_valid = false
    }

    if digit_count > 3 {
        is_valid = false
    }

    if first_char < 'a' || first_char > 'z' {
        is_valid = false
    }

    if is_valid {
        return "Yes"
    } else {
        return "No"
    }
}



