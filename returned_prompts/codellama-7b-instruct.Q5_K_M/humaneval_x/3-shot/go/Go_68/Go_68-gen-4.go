    var result []int = make([]int, 0)
    var smallest_index int = 0
    var smallest_value int = math.MaxInt32
    for i, v := range arr{
        if v%2==0 && v < smallest_value{
            smallest_value = v
            smallest_index = i
        }
    }

    if smallest_value != math.MaxInt32{
        result = append(result, smallest_value)
        result = append(result, smallest_index)
    }
    return result
}



