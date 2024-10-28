    if len(arr) == 1 {
        return 0
    }
    left := 0
    right := len(arr) - 1
    min_changes := 0
    for left < right {
        if arr[left] == arr[right] {
            left += 1
            right -= 1
        }else {
            min_changes += 1
            arr[left] = arr[right]
        }
    }
    return min_changes
}



