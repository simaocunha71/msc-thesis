    var is_latin_alpha_started bool = false
    var is_three_digits bool = false

    for _, c := range file_name {
        if !is_latin_alpha_started && (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') {
            is_latin_alpha_started = true
        }else if c >= '0' && c <= '9' {
            is_three_digits = true
        }
        if is_three_digits > 3 {
            return "No"
        }
    }

    splited := strings.Split(file_name, ".")
    if len(splited) != 2 {
        return "No"
    }
    if !is_latin_alpha_started {
        return "No"
    }
    if splited[0] == "" {
        return "No"
    }
    if splited[1] != "txt" && splited[1] != "exe" && splited[1] != "dll" {
        return "No"
    }

    return "Yes"
}



