    count := 0
    for i := 0; i < len(s); i++ {
        if i%2 == 0 && strings.ToUpper(string(s[i])) == string(s[i]) {
            count++
        }
    }
    return count
} 