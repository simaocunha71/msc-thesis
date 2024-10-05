    for i := range arr {
        for j := i; j > 0; j-- {
            if arr[i] > arr[j-1] {
                arr[j-1], arr[i] = arr[i], arr[j-1]
                i--
            }
        }
    }

    return arr[len(arr)-k:]
}
