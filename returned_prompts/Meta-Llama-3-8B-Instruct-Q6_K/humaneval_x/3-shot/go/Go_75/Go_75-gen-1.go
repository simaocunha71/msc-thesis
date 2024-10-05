    for i := 2; i < 100; i++ {
        for j := i; j < 100; j++ {
            for k := j; k < 100; k++ {
                if i * j * k == a {
                    return true
                }
            }
        }
    }
    return false
}



