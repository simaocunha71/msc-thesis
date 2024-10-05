    smallest := math.MaxInt64
    smallest_index := -1

    for i, v := range arr {
        if v%2 == 0 && v < smallest {
            smallest = v
            smallest_index = i
        }
    }

    if smallest_index != -1 {
        return []int{smallest, smallest_index}
    }
    return []int{}
}


