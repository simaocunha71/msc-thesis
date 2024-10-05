    if interval1[0] <= interval2[1] && interval1[1] >= interval2[0]{
        start := int(math.Max(float64(interval1[0], interval2[0])))
        end := int(math.Min(float64(interval1[1], interval2[1])))
        length := end - start
        if length > 0 && length % 2 == 1{
            return "YES"
        }
    }
    return "NO"
}



