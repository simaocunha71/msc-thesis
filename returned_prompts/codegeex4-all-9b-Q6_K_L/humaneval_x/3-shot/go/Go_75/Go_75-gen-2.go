    if a < 2 {
        return false
    }
    for i := 2; i <= a/2; i++ {
        if a%i == 0 {
            return false
        }
    }
    return true
}



