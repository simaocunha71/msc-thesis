    for i := 0; i < len(a)-len(b)+1; i++ {
        if a[i:i+len(b)] == b || a[i:i+len(b)] == b[len(b)-1:] + b[:len(b)-1] {
            return true
        }
    }
    return false
}



