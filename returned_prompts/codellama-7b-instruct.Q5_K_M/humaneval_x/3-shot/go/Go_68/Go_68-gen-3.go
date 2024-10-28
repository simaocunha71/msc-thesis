    var smallest_value int = math.MaxInt32
    var smallest_index int = -1
    for i, v := range arr {
        if v%2 == 0 && v < smallest_value {
            smallest_value = v
            smallest_index = i
        }
    }

    return []int{smallest_value, smallest_index}
}



