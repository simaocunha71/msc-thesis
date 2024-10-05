    start := max(interval1[0], interval2[0])
    end := min(interval1[1], interval2[1])
    if end < start {
        return "NO"
    }
    length := end - start + 1
    if isPrime(length) {
        return "YES"
    }
    return "NO"
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    if n == 2 {
        return true
    }
    if n % 2 == 0 {
        return false
    }
    limit := int(math.Sqrt(float64(n)))
    for i := 3; i <= limit; i += 2 {
        if n % i == 0 {
            return false
        }
    }
    return true
}





