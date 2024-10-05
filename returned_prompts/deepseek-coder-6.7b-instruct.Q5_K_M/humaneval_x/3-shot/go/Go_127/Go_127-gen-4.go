    start := Max(interval1[0], interval2[0])
    end := Min(interval1[1], interval2[1])
    length := end - start + 1

    if start > end {
        return "NO"
    }

    if IsPrime(length) {
        return "YES"
    } else {
        return "NO"
    }
}

func Max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func Min(a, b int) int {
    if a < b {
        return a
        }
    return b
}

func IsPrime(n int) bool {
    if n <= 1 {
        return false
    }

    for i := 2; i * i <= n; i++ {
        if n % i == 0 {
            return false
        }
    }

    return true
}


