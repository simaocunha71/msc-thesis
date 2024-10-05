    for i := 0; i < len(b); i++ {
        for j := 0; j < len(b); j++ {
            var temp string = b[j:]
            if temp+len(temp[:i]) == a {
                return true
            }
        }
    }
    return false
}