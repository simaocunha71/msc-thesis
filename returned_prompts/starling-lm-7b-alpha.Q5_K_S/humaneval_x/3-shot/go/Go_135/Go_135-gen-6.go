    index := -1
    prev_max := -1
    for i, v := range arr {
        if v > prev_max {
            prev_max = v
        }else if index == -1 {
            index = i
        }
    }
    return index
}



