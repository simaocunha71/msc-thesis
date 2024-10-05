    for i := 2; i <= 10; i++ {
        if a % i == 0 {
            for j := 2; j < i; j++ {
                if a % j == 0 {
                    return false
                }
            }
            return true
        }
    }
    return false
}



