    start = math.Max(interval1[0], interval2[0])
    end = math.Min(interval1[1], interval2[1])
    if start > end {
        return "NO"
    }
    length = end - start + 1
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