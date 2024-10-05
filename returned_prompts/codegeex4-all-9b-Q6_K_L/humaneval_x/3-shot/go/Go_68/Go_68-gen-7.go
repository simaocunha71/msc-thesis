    if len(arr) == 0 {
        return []int{}
    }

    min_value := math.MaxInt64
    min_index := -1

    for i, value := range arr {
        if value % 2 == 0 && value < min_value {
            min_value = value
            min_index = i
        }
    }

    if min_index == -1 {
        return []int{}
    }

    return []int{arr[min_index], min_index}
}



