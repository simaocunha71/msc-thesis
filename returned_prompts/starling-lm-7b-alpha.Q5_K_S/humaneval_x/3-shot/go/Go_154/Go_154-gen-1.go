    b_len := len(b)
    for i := 0; i < len(a); i++ {
        if len(a)-i < b_len {
            break
        }
        if a[i:len(a)-i] == b {
            return true
        }
    }

    return false
}



