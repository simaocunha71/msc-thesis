    b_length := len(b)
    if len(a) < b_length {
        return false
    }
    for i := 0; i < len(a)-b_length+1; i++ {
        if a[i:i+b_length] == b {
            return true
        }
    }
    for i := 0; i < b_length; i++ {
        if CycpatternCheck(a, b[i:]+b[:(len(b)-i):]) {
            return true
        }
    }
    return false
}



