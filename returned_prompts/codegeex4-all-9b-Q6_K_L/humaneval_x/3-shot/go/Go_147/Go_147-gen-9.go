    a := make([]int, n)
    count := 0

    for i := 0; i < n; i++ {
        a[i] = i * i - i + 1
        if i > 1 {
            for j := 0; j < i; j++ {
                for k := j + 1; k < i; k++ {
                    if (a[i] + a[j] + a[k]) % 3 == 0 {
                        count++
                    }
                }
            }
        }
    }
    return count
}

