    for i := 0; i < (1<<12); i++ {
        sum := 0
        for j := 0; j < 4; j++ {
            if (i & (1<<j)) != 0 {
                sum += 2*j
            }
        }
        if sum == n {
            return true
        }
    }
    return false
}



