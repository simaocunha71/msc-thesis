    if n % 2 != 0 {
        return false
    }

    for i := 0; i < n/4; i++ {
        for j := i + 1; j < n/3; j++ {
            for k := j + 1; k < n/2; k++ {
                for l := k + 1; l < n; l++ {
                    if i + j + k + l == n {
                        return true
                    }
                }
            }
        }
    }
    return false
}



