    sort.Ints(arr)
    for i := 0; i < len(arr)-1; i++ {
        if arr[i] == arr[i+1] {
            continue
        }

        if arr[i] < arr[i+1] {
            return true
        }
    }

    return false
}



