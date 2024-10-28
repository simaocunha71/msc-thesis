    a := make([]int, 0)

    for i := 1; i <= n; i++ {
        a = append(a, i*i-i+1)
    }

    count := 0

    for i := 0; i < len(a); i++ {
        for j := i + 1; j < len(a); j++ {
            for k := j + 1; k < len(a); k++ {
                if (a[i] + a[j] + a[k]) % 3 == 0 {
                    count += 1
                }
            }
        }
    }

    return count
}



