    start = math.Max(interval1[0], interval2[0])
    end = math.Min(interval1[1], interval2[1])
    if start > end {
        return "NO"
    }
    return "YES" if isPrime(end - start + 1) else "NO"
}

func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}