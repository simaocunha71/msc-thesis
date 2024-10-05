    count := 0
    for i := 0; i < len(s); i += 2 {
        if strings.ToUpper(string(s[i])) == "U" || strings.ToUpper(string(s[i])) == "E" || strings.ToUpper(string(s[i])) == "I" || strings.ToUpper(string(s[i])) == "O" || strings.ToUpper(string(s[i])) == "A" {
            count++
        }
    }
    return count
}