    var smallest int = math.MaxInt32
    var index int = -1

    for i, v := range arr {
        if v%2 == 0 && v < smallest {
            smallest = v
            index = i
        }
    }

    if index == -1 {
        return []int{}
    }

    return []int{smallest, index}
}



