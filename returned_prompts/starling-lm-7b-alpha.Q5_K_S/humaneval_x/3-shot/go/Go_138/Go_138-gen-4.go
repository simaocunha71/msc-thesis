    for i := 1; i < (n / 2) + 1; i++ {
        for j := 1; j < (n / 2) + 1; j++ {
            for k := 1; k < (n / 2) + 1; k++ {
                for l := 1; l < (n / 2) + 1; l++ {
                    if i + j + k + l == n {
                        return true
                    }
                }
            }
        }
    }
    return false
}



