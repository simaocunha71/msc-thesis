    smallestEvenValue := math.MaxInt64
    smallestEvenIndex := -1
    for i, v := range arr {
        if v < smallestEvenValue && v % 2 == 0 {
            smallestEvenValue = v
            smallestEvenIndex = i
        }
    }
    if smallestEvenIndex == -1 {
        return []int{}
    }
    return []int{smallestEvenValue, smallestEvenIndex}
}



