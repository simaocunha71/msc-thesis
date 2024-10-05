    var a []int = make([]int, n)
    for i := 1; i <= n; i++ {
        a[i-1] = (i * i) - i + 1
    }

    var count int = 0
    for i := 0; i < n; i++ {
        for j := i + 1; j < n; j++ {
            for k := j + 1; k < n; k++ {
                if (a[i] + a[j] + a[k])%3 == 0 {
                    count++
                }
            }
        }
    }
    return count
}



