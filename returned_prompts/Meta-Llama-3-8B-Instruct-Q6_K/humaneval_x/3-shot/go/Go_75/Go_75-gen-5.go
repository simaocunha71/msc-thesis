    for i := 2; i < 10; i++ {
        for j := i + 1; j < 10; j++ {
            for k := j + 1; k < 10; k++ {
                if i*j*k == a {
                    return true
                }
            }
        }
    }
    return false
} 



