    var result int

    for i := 0; i < len(s); i += 2 {
        if strings.Contains("AEIOU", strings.ToUpper(string(s[i]))) {
            result += 1
        }
    }
    return result
}



