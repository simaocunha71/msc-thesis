    for _, c := range b {
        if len(b) > len(a) {
            return false
        }

        if a.Index(b) >= 0 {
            return true
        }

        b = string(c) + b[:len(b)-1]
    }
    return false
}



