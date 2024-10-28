    start := max(interval1[0], interval2[0])
    end := min(interval1[1], interval2[1])

    if end < start {
        return "NO"
    }
    if end == start {
        return "NO"
    }
    if end - start == 1 {
        return "NO"
    }
    for i := 2; i <= end-start; i++ {
        if isPrime(i) {
            return "YES"
        }
    }
    return "NO"
}



