    if len(txt) == 0 {
        return false
    }
    last_char := string(txt[len(txt)-1])
    if last_char == " " {
        return false
    }
    if strings.Contains(last_char, " ") {
        return false
    }
    if strings.Contains(last_char, ".") {
        return false
    }
    if strings.Contains(last_char, ",") {
        return false
    }
    if strings.Contains(last_char, "!") {
        return false
    }
    if strings.Contains(last_char, "?") {
        return false
    }
    if strings.Contains(last_char, "'") {
        return false
    }
    if strings.Contains(last_char, "\"") {
        return false
    }
    if strings.Contains(last_char, ";") {
        return false
    }
    if strings.Contains(last_char, ":") {
        return false
    }
    if strings.Contains(last_char, "/") {
        return false
    }
    if strings.Contains(last_char, "\\") {
        return false
    }
    if strings.Contains(last_char, "(") {
        return false
    }
    if strings.Contains(last_char, ")") {
        return false
    }
    if strings.Contains(last_char, "{") {
        return false
    }
    if strings.Contains(last_char, "}") {
        return false
    }
    if strings.Contains(last_char, "[") {
        return false
    }
    if strings.Contains(last_char, "]") {
        return false
    }
    if strings.Contains(last_char, "<") {
        return false
    }
    if strings.Contains(last_char, ">") {
        return false
    }
    if strings.Contains(last_char, "+") {
        return false
    }
    if strings.Contains(last_char, "-") {
        return false
    }
    if strings.Contains(last_char, "*") {