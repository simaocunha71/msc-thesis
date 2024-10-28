    start := max(interval1[0], interval2[0])
    end := min(interval1[1], interval2[1])
    length := end - start + 1

    if length <= 1 {
        return "NO"
    }

    for i := 2; i*i <= length; i++ {
        if length%i == 0 {
            return "NO"
        }
    }
    return "YES"
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



