    length := len(s)
    if length == 2 || length == 3 {
        return true
    }
    if length % 2 == 0 || length % 3 == 0 {
        return false
    }
    for i := 5; i * i <= length; i += 6 {
        if length % i == 0 {
            return false
        }
    }
    return true
}



