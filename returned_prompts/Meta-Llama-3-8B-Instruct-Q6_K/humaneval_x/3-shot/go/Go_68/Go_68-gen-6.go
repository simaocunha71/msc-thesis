    minEvenIndex := -1
    minEvenValue := math.MaxInt64
    for i, v := range arr {
        if v % 2 == 0 && v < minEvenValue {
            minEvenIndex = i
            minEvenValue = v
        }
    }
    if minEvenIndex != -1 {
        return []int{minEvenValue, minEvenIndex}
    }
    return []int{}
}