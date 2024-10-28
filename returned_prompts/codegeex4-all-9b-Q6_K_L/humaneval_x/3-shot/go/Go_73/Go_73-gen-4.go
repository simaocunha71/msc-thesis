    count := 0
    i, j := 0, len(arr)-1

    for i < j {
        if arr[i] != arr[j] {
            count++
            if arr[i] > arr[j] {
                arr[j] = arr[i]
            } else {
                arr[i] = arr[j]
            }
        }
        i++
        j--
    }
    return count
}



