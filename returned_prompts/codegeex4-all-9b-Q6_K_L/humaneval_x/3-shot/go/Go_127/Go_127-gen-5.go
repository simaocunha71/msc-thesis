    var intersection []int
    intersection = append(intersection, max(interval1[0], interval2[0]))
    intersection = append(intersection, min(interval1[1], interval2[1]))

    if intersection[0] <= intersection[1] {
        if isPrime(intersection[1] - intersection[0]) {
            return "YES"
        }else {
            return "NO"
        }
    }else {
        return "NO"
    }
}

func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    if n == 2 {
        return true
    }
    if n%2 == 0 {
        return false
    }
    for i := 3; i*i <= n; i += 2 {
        if n%i == 0 {
            return false
        }
    }
    return true
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}


