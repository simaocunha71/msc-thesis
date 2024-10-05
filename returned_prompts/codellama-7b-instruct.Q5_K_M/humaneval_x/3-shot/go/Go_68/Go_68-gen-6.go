    min := math.MaxInt32
    for i := 0; i < len(arr); i++ {
        if arr[i]%2 == 0 && arr[i] < min{
            min = arr[i]
        }
    }

    for i := 0; i < len(arr); i++ {
        if arr[i]%2 == 0 && arr[i] == min{
            return []int{min, i}
        }
    }
    return []int{}
}



