    for i := 0; i < len(arr); i++ {
        for j := i + 1; j < len(arr); j++ {
            if arr[i] > arr[j] {
                arr[i], arr[j] = arr[j], arr[i]
                goto A
            }
        }
    }

    for i := range arr {
        if arr[i]%2 == 0 {
            return []int{arr[i], i}
        }
    }

    return []int{}
}
