    result := make([]rune, 0)

    for i := 0; i < len(s); i += 3 {
        if i+3 <= len(s) {
            result = append(result, []rune(s[i:i+3])...)
        } else {
            result = append(result, []rune(s[i:])...)
        }
    }
    return string(result)
}



