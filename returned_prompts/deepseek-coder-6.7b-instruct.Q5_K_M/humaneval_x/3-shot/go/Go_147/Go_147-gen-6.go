    var count int = 0
    var arr = make([]int, n+1)
    for i := 1; i <= n; i++ {
        arr[i] = i*i - i + 1
    }

    for i := 1; i <= n-2; i++ {
        for j := i + 1; j <= n-1; j++ {
            for k := j + 1; k <= n; k++ {
                if (arr[i]+arr[j]+arr[k])%3 == 0 {
                    count++
                }
            }
        }
    }
    return count
}



