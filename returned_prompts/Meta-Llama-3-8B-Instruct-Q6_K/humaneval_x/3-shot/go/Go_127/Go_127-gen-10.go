    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    if start > end {
        return "NO"
    }
    length := end - start + 1
    if length == 1 {
        return "NO"
    }
    for i := 2; i <= int(math.Sqrt(float64(length))); i++ {
        if length%i == 0 {
            return "NO"
        }
    }
    return "YES"
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