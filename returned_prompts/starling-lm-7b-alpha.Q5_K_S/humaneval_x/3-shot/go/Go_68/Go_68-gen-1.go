    smallest_value := math.MaxInt32
    smallest_index := -1
    for i,v := range arr{
        if v%2 == 0 && v < smallest_value {
            smallest_value = v
            smallest_index = i
        }
    }

    return []int{smallest_value, smallest_index}
}



