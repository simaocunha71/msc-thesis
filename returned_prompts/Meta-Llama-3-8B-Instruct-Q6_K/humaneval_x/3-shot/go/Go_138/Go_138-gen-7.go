    for i := 2; i <= n/2; i += 2 {
        for j := 2; j <= n/2; j += 2 {
            for k := 2; k <= n/2; k += 2 {
                for m := 2; m <= n/2; m += 2 {
                    if i+j+k+m == n {
                        return true
                    }
                }
            }
        }
    }
    return false
}