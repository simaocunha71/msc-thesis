    last_char := strings.ToLower(string(txt[len(txt)-1]))
    if last_char >= "a" && last_char <= "z" {
        return true
    }
    return false
}



