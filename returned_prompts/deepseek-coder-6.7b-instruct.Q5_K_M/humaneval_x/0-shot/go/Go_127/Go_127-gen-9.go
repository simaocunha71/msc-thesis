
    // Check if the intervals intersect
    if interval1[0] > interval2[1] || interval2[0] > interval1[1] {
        return "NO"
    }

    // Calculate the length of the intersection
    start := max(interval1[0], interval2[0])
    end := min(interval1[1], interval2[1])
    length := end - start + 1

    // Check if the length is a prime number
    if length < 2 {
        return "NO"
    }
    for i := 2; i*i <= length; i++ {
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

```














































































































































































































































































