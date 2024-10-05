    if len(lst) < 2 {
        return nil
    }

    sort.Ints(lst)

    smallest := math.MaxInt64
    secondSmallest := math.MaxInt64

    for _, v := range lst {
        if v < smallest {
            secondSmallest = smallest
            smallest = v
        } else if v < secondSmallest && v != smallest {
            secondSmallest = v
        }
    }

    if secondSmallest == math.MaxInt64 {
        return nil
    }

    return secondSmallest
}



