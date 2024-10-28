    result := 0
    for i := 1; i <= n; i++ {
        for j := i + 1; j <= n; j++ {
            for k := j + 1; k <= n; k++ {
                sum := i * i - i + 1 + j * j - j + 1 + k * k - k + 1
                if sum % 3 == 0 {
                    result += 1
                }
            }
        }
    }
    return result
}

