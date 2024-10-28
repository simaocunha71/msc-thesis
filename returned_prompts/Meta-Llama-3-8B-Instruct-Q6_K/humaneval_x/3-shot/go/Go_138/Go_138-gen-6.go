    for i := 2; i <= n/2; i++ {
        if i % 2 == 0 {
            for j := 2; j <= n/2; j++ {
                if j % 2 == 0 {
                    for k := 2; k <= n/2; k++ {
                        if k % 2 == 0 {
                            for l := 2; l <= n/2; l++ {
                                if l % 2 == 0 {
 if i+j+k+l == n {
 return true
 }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    return false
} 





