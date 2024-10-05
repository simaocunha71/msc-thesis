    for i:= 0; i < len(b); i++ {
        var pattern string = b
        for i := 0; i < len(pattern); i++ {
            pattern = string(pattern[1]) + pattern[:len(pattern)-1]
            if strings.Contains(a, pattern) {
                return true
            }
        }
    }
    return false
}



