    result := 1
    for i := 1; i <= n; i++ {
        result *= math.Fact(int64(i))
    }
    return int(result)
}

func math.Fact(n int64) int64 {
    if n == 0 {
        return 1
    }
    return int64(n) * math.Fact(n-1)
}