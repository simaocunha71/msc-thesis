    min := 1<<63 - 1
    index := -1

    for i, v := range arr {
        if v < min && v%2 == 0 {
            min = v
            index = i
        }
    }

    if index == -1 {
        return []int{}
    }

    return []int{min, index}
}



