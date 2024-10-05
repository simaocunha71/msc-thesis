    smallest := math.MaxInt64
    index := -1
    for i, v := range arr {
        if v % 2 == 0 && v < smallest {
            smallest = v
            index = i
        }
    }
    if index == -1 {
        return []int{}
    }
    return []int{smallest, index}
}


B:
    smallest := math.MaxInt64
    index := -1
    for i, v := range arr {
        if v < smallest && v % 2 == 0 {
            smallest = v
            index = i
        }
    }
    if index == -1 {
        return []int{}
    }
    return []int{smallest, index}
}


C:
    smallest := math.MaxInt64
    index := -1
    for i, v := range arr {
        if v < smallest && v % 2 == 0 {
            smallest = v
            index = i
        }
    }
    if index == -1 {
        return []int{}
    }
    return []int{smallest, index}
}


D:
    smallest := math.MaxInt64
    index := -1
    for i, v := range arr {
        if v % 2 == 0 && v < smallest {
            smallest = v
            index = i
        }
    }
    if index == -1 {
        return []int{}
    }
    return []int{smallest, index}
}


E:
    smallest := math.MaxInt64
    index := -1
    for i, v := range arr {
        if v < smallest && v % 2 == 0 {
            smallest = v
            index = i
        }
    }
    if index == -1 {
        return []int{}
    }
    return []int{smallest