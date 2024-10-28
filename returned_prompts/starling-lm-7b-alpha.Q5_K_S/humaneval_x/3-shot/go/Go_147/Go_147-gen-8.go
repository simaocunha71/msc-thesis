    result := 0
    for i := 1; i <= n; i++ {
        j := i + 1
        k := j + 1
        if (i * i - i + 1) % 3 == 0 && (j * j - j + 1) % 3 == 0 && (k * k - k + 1) % 3 == 0 {
            result += 1
        }
    }
    return result
}



