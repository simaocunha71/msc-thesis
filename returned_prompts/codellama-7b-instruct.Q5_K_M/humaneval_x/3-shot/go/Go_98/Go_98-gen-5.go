    var result int = 0
    s = strings.ToUpper(s)
    for i := 0; i < len(s); i += 2 {
        if string(s[i]) == "A" || string(s[i]) == "E" || string(s[i]) == "I" || string(s[i]) == "O" || string(s[i]) == "U" {
            result += 1
        }
    }
    return result
}



