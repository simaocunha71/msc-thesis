    if a < 100 {
        return false
    }

    for i := 2; i < 100; i++ {
        if a % i == 0 {
            if a / i < 100 {
                return false
            }
            for j := 2; j < 100; j++ {
                if a / i % j == 0 {
                    return false
                }
            }
            return true
        }
    }
    return false
}



