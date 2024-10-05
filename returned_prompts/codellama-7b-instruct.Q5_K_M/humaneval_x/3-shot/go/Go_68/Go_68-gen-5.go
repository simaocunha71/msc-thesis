    var result = make([]int,2)
    var smallest_value = math.MaxInt32
    var smallest_index = -1

    for i := 0; i < len(arr); i++{
        if arr[i]%2 == 0 && arr[i] < smallest_value{
            smallest_value = arr[i]
            smallest_index = i
        }
    }

    if smallest_index == -1{
        return []int{}
    }

    result[0] = smallest_value
    result[1] = smallest_index
    return result
}



