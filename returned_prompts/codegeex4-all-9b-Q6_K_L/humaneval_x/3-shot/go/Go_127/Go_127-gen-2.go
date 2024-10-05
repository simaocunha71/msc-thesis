    start := max(interval1[0], interval2[0])
    end := min(interval1[1], interval2[1])
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
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
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



