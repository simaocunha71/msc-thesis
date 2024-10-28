    var count int
    a := make([]int, n)
    for i := 0; i < n; i++ {
        a[i] = i * i - i + 1
    }
    for i := 0; i < n; i++ {
        for j := i + 1; j < n; j++ {
            for k := j + 1; k < n; k++ {
                if (a[i] + a[j] + a[k]) % 3 == 0 {
                    count++
                }
            }
        }
    }
    return count
}