    for i := range arr {
        if arr[i]%2 == 0 {
            return []int{arr[i], i}
        }
    }
    return []int{}
}

