    var count int
    for i := 1; i < n; i++ {
        for j := i + 1; j < n; j++ {
            for k := j + 1; k <= n; k++ {
                if (i*i-i+1)+(j*j-j+1)+(k*k-k+1)%3 == 0 {
                    count++
                }
            }
        }
    }
    return count
}