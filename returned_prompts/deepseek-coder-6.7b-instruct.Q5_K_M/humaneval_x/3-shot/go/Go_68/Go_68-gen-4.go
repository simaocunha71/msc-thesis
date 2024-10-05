    smallestEvenValue, smallestEvenIndex := math.MaxInt64, -1

    for i, v := range arr {
        if v < smallestEvenValue && v % 2 == 0 {
            smallestEvenValue, smallestEvenIndex = v, i
        }
    }

    if smallestEvenIndex == -1 {
        return []int{}
    }

    return []int{smallestEvenValue, smallestEvenIndex}
}



