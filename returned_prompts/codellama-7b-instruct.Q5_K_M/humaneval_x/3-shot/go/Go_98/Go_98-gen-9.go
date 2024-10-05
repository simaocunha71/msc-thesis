    var count int
    for i := 0; i < len(s); i += 2 {
        c := strings.ToUpper(string(s[i]))
        if c == "A" || c == "E" || c == "I" || c == "O" || c == "U" {
            count += 1
        }
    }
    return count
}



