    if interval1[0] > interval2[1] || interval2[0] > interval1[1] {
        return "NO"
    }
    start := max(interval1[0], interval2[0])
    end := min(interval1[1], interval2[1])
    length := end - start + 1
    if isPrime(length) {
        return "YES"
    }else{
        return "NO"
    }
}

func max(a, b int) int {
    if a > b {
        return a
    }else{
        return b
    }
}

func min(a, b int) int {
    if a < b {
        return a
    }else{
        return b
    }
}

func isPrime(n int) bool {
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n % i == 0 {
            return false
        }
    }
    return true
}



