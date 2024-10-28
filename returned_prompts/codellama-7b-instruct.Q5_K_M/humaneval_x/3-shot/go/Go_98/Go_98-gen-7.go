    count := 0
    for i := 0; i < len(s); i += 2 {
        if strings.Contains("AEIOU", strings.ToUpper(string(s[i]))) {
            count += 1
        }
    }
    return count
}



