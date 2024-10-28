    for i := 2; i <= 10; i++ {
        for j := i; j <= 10; j++ {
            for k := j; k <= 10; k++ {
                if i * j * k == a {
                    return true
                }
            }
        }
    }
    return false
}