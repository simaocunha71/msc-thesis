    n := len(arr)
    left, right := 0, n-1
    changes := 0

    for left < right {
        if arr[left] != arr[right] {
            changes++
            for i := left; i < right; i++ {
                if arr[i] == arr[right] {
                    arr[i], arr[left] = arr[left], arr[i]
                    left++
                    break
                }
            }
        } else {
            left++
            right--
        }
    }
    return changes
}