    left, right := 0, len(arr) - 1
    min_changes := 0

    for left < right {
        if arr[left] == arr[right] {
            left += 1
            right -= 1
        }else{
            min_changes += 1
            left += 1
            right -= 1
        }
    }

    return min_changes
}



