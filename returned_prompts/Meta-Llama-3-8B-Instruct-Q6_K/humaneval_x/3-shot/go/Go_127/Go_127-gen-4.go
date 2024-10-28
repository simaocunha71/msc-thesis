    start = int(math.Max(float64(interval1[0]),float64(interval2[0])))
    end = int(math.Min(float64(interval1[1]),float64(interval2[1])))
    if start > end {
        return "NO"
    }
    length := end - start + 1
    for i := 2; i <= int(math.Sqrt(float64(length))); i++ {
        if length%i == 0 {
            return "NO"
        }
    }
    return "YES"
}