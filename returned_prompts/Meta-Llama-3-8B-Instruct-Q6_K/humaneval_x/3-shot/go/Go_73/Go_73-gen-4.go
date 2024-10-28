    n := len(arr)
    left, right := 0, n-1
    changes := 0

    for left < right {
        if arr[left] != arr[right] {
            changes++
        }
        left++
        right--
    }

    return changes
}