    result := 0
    for i := 0; i < len(s); i++ {
        if i % 2 == 0 && "AEIOU".ContainsString(string(s[i])) {
            result += 1
        }
    }
    return result
}



