    if a == 1 {
        return false
    }
    for i := 2; i < 10; i++ {
        for j := 2; j < 10; j++ {
            if i * j == a {
                return true
            }
        }
    }
    return false
}



