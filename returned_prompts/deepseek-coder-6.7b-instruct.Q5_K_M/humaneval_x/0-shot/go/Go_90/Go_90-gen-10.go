    if len(lst) <= 1 {
        return nil
    }
    sort.Ints(lst)
    smallest := math.MaxInt64
    nextSmallest := math.MaxInt64
    for _, v := range lst {
        if v < smallest {
            nextSmallest = smallest
            smallest = v
        } else if v > smallest && v < nextSmallest {
            nextSmallest = v
        }
    }
    if nextSmallest == math.MaxInt64 {
        return nil
    }
    return nextSmallest
}

