func LargestSmallestIntegers(lst []int) [2]interface{}{
    neg := math.MaxInt64
    pos := math.MinInt64
    for _, v := range lst {
        if v < 0 && v < neg {
            neg = v
        } else if v > 0 && v > pos {
            pos = v
        }
    }
    if neg == math.MaxInt64 {
        neg = nil
    }
    if pos == math.MinInt64 {
        pos = nil
    }
    return [2]interface{}{neg, pos}
}