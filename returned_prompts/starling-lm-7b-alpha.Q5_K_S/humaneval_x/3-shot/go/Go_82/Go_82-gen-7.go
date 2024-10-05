    length := len(s)
    if length == 2 || length == 3 {
        return true
    }
    for i := 2; i < length; i++ {
        if length % i == 0 {
            return false
        }
    }
    return true
}



