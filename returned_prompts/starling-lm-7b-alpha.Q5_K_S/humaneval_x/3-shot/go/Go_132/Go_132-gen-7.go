    for i := 0; i < len(s); i++ {
        if s[i] == '[' && s[i + 1] == '[' {
            return true
        }
    }
    return false
}



