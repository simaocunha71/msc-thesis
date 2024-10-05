    sort.Ints(arr)
    for i, num := range arr {
        if i == 0 {
            continue
        }
        if num > arr[i-1] {
            return true
        }
    }
    return false
}



