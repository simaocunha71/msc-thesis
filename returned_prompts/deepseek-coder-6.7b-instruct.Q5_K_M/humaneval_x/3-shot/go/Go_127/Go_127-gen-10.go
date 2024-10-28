    start := int(math.Max(float64(interval1[0]), float64(interval2[0])))
    end := int(math.Min(float64(interval1[1]), float64(interval2[1])))
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



