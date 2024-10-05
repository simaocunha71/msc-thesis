    for i := 0; i < len(b); i++ {
        for j := i; j < len(b); j++ {
            sub := b[j-i:j+1]
            if a == sub {
                return true
            }
        }
    }
    return false
}