    // get the max start and min end of the intersection
    start := max(interval1[0], interval2[0])
    end := min(interval1[1], interval2[1])

    // if the end is greater than or equal to start, they intersect
    if end >= start {
        // calculate length of intersection
        length := end - start + 1
        // check if length is a prime number
        if isPrime(length) {
            return "YES"
        }
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
    for i := 2; i*i <= n; i++ {
        if n % i == 0 {
            return false
        }
    }
    return true
}



