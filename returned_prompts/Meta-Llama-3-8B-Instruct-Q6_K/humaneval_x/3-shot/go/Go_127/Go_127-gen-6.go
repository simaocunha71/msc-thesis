    start1, end1 := interval1[0], interval1[1]
    start2, end2 := interval2[0], interval2[1]

    var start, end int
    if start1 <= start2 {
        start = start1
    } else {
        start = start2
    }
    if end1 >= end2 {
        end = end1
    } else {
        end = end2
    }

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