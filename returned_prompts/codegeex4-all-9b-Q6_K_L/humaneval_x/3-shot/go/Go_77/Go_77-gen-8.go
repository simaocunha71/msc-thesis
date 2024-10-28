    if a < 0 {
        return false
    }
    for i := 1; i*i*i <= a; i++ {
        if i*i*i == a {
            return true
        }
    }
    return false
}



