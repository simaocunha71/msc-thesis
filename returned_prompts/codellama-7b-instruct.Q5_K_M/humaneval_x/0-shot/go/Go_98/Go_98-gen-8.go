    for i := 0; i < len(s); i += 2 {
        if !strings.ContainsAny(s[i:i+1], "AEIOU") {
            continue A
        }
        if strings.ToUpper(s[i:i+1]) == s[i:i+1] {
            return 1
        }
    }
    return 0
}

