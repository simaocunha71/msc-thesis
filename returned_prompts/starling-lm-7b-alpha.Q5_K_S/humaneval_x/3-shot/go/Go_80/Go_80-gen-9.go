    if len(s) < 3 {
        return false
    }
    count := 0
    for i := 0; i < len(s); i++ {
        for j := i + 1; j < len(s); j++ {
            for k := j + 1; k < len(s); k++ {
                if s[i] == s[j] && s[j] == s[k] {
                    count += 1
                }
            }
        }
    }
    return count == 0
}



