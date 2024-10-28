    start := int(math.Max(float64(interval1[0]), float64(interval2[0])))
    end := int(math.Min(float64(interval1[1]), float64(interval2[1])))

    if start > end {
        return "NO"
    }

    if end-start == 0 {
        return "NO"
    }

    if math.Mod(float64(end-start), 2) == 0 {
        return "YES"
    }

    return "NO"
}



