    length := len(s)
    for i := 2; i * i <= length; i++ {
        if length % i == 0 {
            return false
        }
    }
    return true
}



