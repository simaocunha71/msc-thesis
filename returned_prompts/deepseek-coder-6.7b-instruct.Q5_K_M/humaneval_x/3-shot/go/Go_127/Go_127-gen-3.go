    var start int = max(interval1[0], interval2[0])
    var end int = min(interval1[1], interval2[1])

    if start > end {
        return "NO"
    }

    length := end - start + 1

    if isPrime(length) {
        return "YES"
    } else {
        return "NO"
    }
}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}

func isPrime(n int) bool {
    if n < 2 {
        return false
    }
    for i := 2; i*i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}



