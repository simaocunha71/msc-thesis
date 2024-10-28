    smallestEven := math.MaxInt64
    smallestEvenIndex := -1

    for i, v := range arr {
        if v < smallestEven && v%2 == 0 {
            smallestEven = v
            smallestEvenIndex = i
        }
    }

    if smallestEvenIndex == -1 {
        return []int{}
    }

    return []int{smallestEven, smallestEvenIndex}
}



