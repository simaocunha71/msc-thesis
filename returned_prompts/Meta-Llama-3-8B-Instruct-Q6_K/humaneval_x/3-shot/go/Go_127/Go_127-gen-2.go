    start = int(math.Max(float64(interval1[0]), float64(interval2[0])))
    end = int(math.Min(float64(interval1[1]), float64(interval2[1])))
    if start > end {
        return "NO"
    }
    length := end - start + 1
    if isPrime(length) {
        return "YES"
    }
    return "NO"
}

func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i * i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}