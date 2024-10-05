    for i := 0; i < (n/2) + 1; i++ {
        for j := 0; j < (n/2) + 1; j++ {
            for k := 0; k < (n/2) + 1; k++ {
                for l := 0; l < (n/2) + 1; l++ {
                    if i + j + k + l == n && i % 2 == 0 && j % 2 == 0 && k % 2 == 0 && l % 2 == 0 {
                        return true
                    }
                }
            }
        }
    }
    return false
}



