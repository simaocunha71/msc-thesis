    var start int = max(interval1[0], interval2[0])
    var end int = min(interval1[1], interval2[1])

    if start > end {
        return "NO"
    }

    if isPrime(end-start+1) {
        return "YES"
    } else {
        return "NO"
    }
}

func min(x, y int) int {
    if x < y {
        return x
    } else {
        return y
    }
}

func max(x, y int) int {
    if x > y {
        return x
    } else {
        return y
    }
}

func isPrime(n int) bool {
    for i := 2; i < n; i++ {
        if n%i == 0 {
            return false
        }
    }
    return n > 1
}



