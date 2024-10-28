    result := make([]int, 0)
    smallest_value := math.MaxInt32
    for i := 0; i < len(arr); i++ {
        if arr[i] % 2 == 0 && arr[i] < smallest_value {
            smallest_value = arr[i]
        }
    }

    for i := 0; i < len(arr); i++ {
        if arr[i] % 2 == 0 && arr[i] == smallest_value {
            result = append(result, i)
        }
    }

    if len(result) == 0 {
        return []int{}
    } else if len(result) == 1 {
        return []int{smallest_value, result[0]}
    } else {
        return []int{smallest_value, result[0]}
    }
}



