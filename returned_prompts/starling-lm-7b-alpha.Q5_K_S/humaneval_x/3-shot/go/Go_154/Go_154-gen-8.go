    for i := 0; i < len(b); i++ {
        if len(b) <= len(a) {
            if a[:len(b)] == b {
                return true
            } else {
                b = b[1:len(b)]
            }
        } else {
            if a[:len(b)] == b {
                return true
            } else {
                return CycpatternCheck(a[len(b):],b)
            }
        }
    }
    return false
}



