    n := len(arr)
    left, right := 0, n-1
    changes := 0

    for left < right {
        if arr[left] != arr[right] {
            changes++
            if arr[left] < arr[right] {
                right--
            } else {
                left++
            }
        } else {
            left++
            right--
        }
    }

    return changes
}