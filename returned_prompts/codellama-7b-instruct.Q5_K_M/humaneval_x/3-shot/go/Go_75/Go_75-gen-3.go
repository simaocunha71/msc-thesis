    for i := 2; i < 100; i++ {
        for j := 2; j < 100; j++ {
            for k := 2; k < 100; k++ {
                if i*j*k == a {
                    return true
                }
            }
        }
    }
    return false
}



