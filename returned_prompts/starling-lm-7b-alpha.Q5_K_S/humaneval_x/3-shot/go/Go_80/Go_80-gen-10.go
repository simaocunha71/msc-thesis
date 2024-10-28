    if len(s) < 3 {
        return false
    }

    var count int = 0
    for i := 0; i < len(s)-2; i++ {
        if s[i] == s[i+1] && s[i+1] == s[i+2] {
            count += 1
        }
    }
    return count == 0
}



