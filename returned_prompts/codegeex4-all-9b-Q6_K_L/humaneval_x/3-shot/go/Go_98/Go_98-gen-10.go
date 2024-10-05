    count := 0
    s = strings.ToLower(s)
    for i := 0; i < len(s); i += 2 {
        if i%2 == 0 {
            if s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u' {
                count++
            }
        }
    }
    return count
}



