    for i := 1; i < n/2 + 1; i++ {
        if i%2 == 0 {
            if n == i + i + i + i {
                return true
            }
        }
    }
    return false
}



